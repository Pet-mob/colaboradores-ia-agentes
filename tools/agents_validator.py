"""
Validador de AgentS - Monitora e valida execução dos agents
Fornece feedback sobre qualidade dos outputs e mudanças efetivas
"""

import subprocess
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Resultado da validação de um agent"""
    agent_name: str
    output_length: int
    is_valid: bool
    issues: List[str]
    quality_score: float  # 0-100


@dataclass
class ExecutionReport:
    """Relatório completo da execução"""
    demand_title: str
    results: Dict[str, ValidationResult]
    git_changes: Dict[str, int]  # arquivo -> linhas mudadas
    overall_success: bool
    summary: str


def _get_git_changes(repo_path: Path, branch: str) -> Dict[str, int]:
    """
    Retorna dicionário de arquivo -> linhas mudadas
    Compara a branch com main/master
    """
    changes = {}
    
    try:
        # Tenta encontrar a branch base
        result = subprocess.run(
            ["git", "branch", "-a"],
            cwd=str(repo_path),
            capture_output=True,
            text=True
        )
        
        base_branch = "main" if "main" in result.stdout else "master"
        
        # Pega diff stat entre branches
        result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}..{branch}"],
            cwd=str(repo_path),
            capture_output=True,
            text=True
        )
        
        for line in result.stdout.strip().split("\n"):
            if line and "|" in line:
                parts = line.split("|")
                if len(parts) >= 2:
                    filename = parts[0].strip()
                    changes_part = parts[1].strip()
                    # Parse "X insertions(+), Y deletions(-)"
                    try:
                        additions = int(changes_part.split()[0]) if changes_part else 0
                        changes[filename] = additions
                    except (ValueError, IndexError):
                        pass
        
        return changes
    except subprocess.CalledProcessError:
        return {}


def validate_agent_output(agent_name: str, output: str, min_length: int = 50) -> ValidationResult:
    """
    Valida o output de um agent
    Retorna ValidationResult com insights
    """
    issues = []
    output_length = len(output) if output else 0
    quality_score = 100.0
    
    # Check 1: Output vazio
    if not output or output_length < min_length:
        issues.append(f"Output muito curto ({output_length} chars)")
        quality_score -= 40
    
    # Check 2: Output parece ser erro ou aviso
    if output and ("error" in output.lower() or "erro" in output.lower()):
        issues.append("Output contém menção de erro")
        quality_score -= 20
    
    # Check 3: Output muito genérico (provavelmente alucinação do LLM)
    generic_phrases = [
        "i don't have access",
        "i cannot",
        "unable to",
        "não tenho acesso",
        "não consigo",
        "não posso"
    ]
    
    if any(phrase in output.lower() for phrase in generic_phrases):
        issues.append("Output contém limitações do modelo")
        quality_score -= 30
    
    # Check 4: Validar conteúdo específico por tipo de agent
    if agent_name.lower() == "planner":
        required_elements = [
            ("tarefas", ["tarefa", "task", "passo", "step"]),
            ("critérios", ["critério", "criteria", "aceite", "acceptance"]),
            ("tecnologias", ["tecnologia", "tech", "stack", "framework"]),
        ]
        
        for element_name, keywords in required_elements:
            if not any(kw in output.lower() for kw in keywords):
                issues.append(f"Plano faltando: {element_name}")
                quality_score -= 15
    
    elif agent_name.lower() == "developer":
        # Code blocks devem estar presentes
        code_indicators = ["```", "def ", "class ", "function ", "const ", "let "]
        if not any(indicator in output for indicator in code_indicators):
            issues.append("Nenhum bloco de código encontrado")
            quality_score -= 35
        
        if "```" in output:
            code_blocks = output.count("```") // 2
            if code_blocks < 1:
                issues.append(f"Poucos blocos de código: {code_blocks}")
                quality_score -= 20
    
    elif agent_name.lower() == "qa":
        qa_elements = [
            ("bugs", ["bug", "issue", "problema", "problema"]),
            ("veredicto", ["✅", "⚠️", "❌", "aprovado", "reprovado", "approved", "rejected"]),
        ]
        
        for element_name, keywords in qa_elements:
            if not any(kw in output.lower() for kw in keywords):
                issues.append(f"QA Report faltando: {element_name}")
                quality_score -= 20
    
    # Garante que quality_score não fica negativo
    quality_score = max(0, min(100, quality_score))
    is_valid = quality_score >= 40 and output_length >= min_length
    
    return ValidationResult(
        agent_name=agent_name,
        output_length=output_length,
        is_valid=is_valid,
        issues=issues,
        quality_score=quality_score
    )


def generate_validation_report(
    demand_title: str,
    agent_outputs: Dict[str, str],
    repo_path: Path = None,
    branch: str = None
) -> ExecutionReport:
    """
    Gera relatório completo de validação
    """
    
    # Valida cada agent
    results = {}
    all_valid = True
    
    for agent_name, output in agent_outputs.items():
        result = validate_agent_output(agent_name, output)
        results[agent_name] = result
        if not result.is_valid:
            all_valid = False
    
    # Tenta pegar mudanças git
    git_changes = {}
    if repo_path and branch:
        git_changes = _get_git_changes(repo_path, branch)
    
    # Gera summary
    summary_lines = [
        f"\n{'='*70}",
        f"RELATÓRIO DE VALIDAÇÃO - {demand_title}",
        f"{'='*70}\n"
    ]
    
    # Resumo por agent
    for agent_name, result in results.items():
        status_icon = "✅" if result.is_valid else "⚠️"
        summary_lines.append(
            f"{status_icon} {agent_name.upper():15} | "
            f"Score: {result.quality_score:.0f}/100 | "
            f"Output: {result.output_length} chars"
        )
        
        if result.issues:
            for issue in result.issues:
                summary_lines.append(f"   ⚠️ {issue}")
    
    # Resumo de mudanças git
    if git_changes:
        summary_lines.append(f"\n📝 Mudanças no Git:")
        total_lines = 0
        for filename, lines in git_changes.items():
            summary_lines.append(f"   • {filename}: +{lines} linhas")
            total_lines += lines
        summary_lines.append(f"   Total: {total_lines} linhas modificadas")
    else:
        summary_lines.append(f"\n⚠️ Nenhuma mudança detectada no Git")
    
    # Veredicto final
    summary_lines.append(f"\n{'='*70}")
    if all_valid and git_changes and sum(git_changes.values()) > 0:
        summary_lines.append("✅ EXECUÇÃO BEM-SUCEDIDA")
        overall_success = True
    elif all_valid:
        summary_lines.append("⚠️ AGENTS PRODUZIRAM OUTPUT, MAS SEM MUDANÇAS GIT")
        overall_success = False
    else:
        summary_lines.append("❌ EXECUÇÃO COM PROBLEMAS")
        overall_success = False
    
    summary_lines.append(f"{'='*70}\n")
    
    summary = "\n".join(summary_lines)
    
    return ExecutionReport(
        demand_title=demand_title,
        results=results,
        git_changes=git_changes,
        overall_success=overall_success,
        summary=summary
    )


def print_validation_report(report: ExecutionReport):
    """Imprime o relatório de forma formatada"""
    print(report.summary)
    
    # Detalhes adicionais
    print("\n📋 DETALHES POR AGENT:")
    for agent_name, result in report.results.items():
        print(f"\n  {agent_name.upper()}")
        print(f"  {'─'*60}")
        print(f"  Score: {result.quality_score:.0f}/100")
        print(f"  Output: {result.output_length} caracteres")
        
        if not result.issues:
            print(f"  ✅ Nenhum problema detectado")
        else:
            print(f"  Problemas encontrados:")
            for issue in result.issues:
                print(f"    • {issue}")


if __name__ == "__main__":
    # Teste simples
    test_outputs = {
        "Planner": "# Plano\n\n1. Tarefa 1\n2. Tarefa 2\n\n## Critérios\n- Aceite 1",
        "Developer": "```python\ndef hello():\n    return 'Hello'\n```",
        "QA": "## Bugs encontrados\n- Bug 1\n\n✅ Aprovado"
    }
    
    report = generate_validation_report("Test Demand", test_outputs)
    print_validation_report(report)
