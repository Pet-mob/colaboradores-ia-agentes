#!/usr/bin/env python
"""
Debug dos Agents - Encontra e executa a validação de uma demanda
"""

from pathlib import Path
from tools.agents_validator import (
    validate_agent_output,
    generate_validation_report,
    print_validation_report,
    _get_git_changes
)
from tools.git_manager import _get_project_repo, _extract_project, get_branch_name


def find_demands(status=None):
    """Lista todas as demandas disponíveis"""
    demands_dir = Path("demands")
    demands = []
    
    for demand_file in demands_dir.rglob("*.md"):
        # Extrai status do path
        if "pending" in str(demand_file):
            demand_status = "pending"
        elif "in_progress" in str(demand_file):
            demand_status = "in_progress"
        elif "done" in str(demand_file):
            demand_status = "done"
        else:
            demand_status = "unknown"
        
        if status is None or demand_status == status:
            demands.append({
                "file": demand_file,
                "name": demand_file.stem,
                "status": demand_status
            })
    
    return sorted(demands, key=lambda x: x["name"])


def show_demand_summary(filepath: Path):
    """Exibe um resumo rápido da demanda"""
    content = filepath.read_text(encoding="utf-8")
    
    lines = content.split("\n")
    title = lines[0].replace("# Demanda:", "").strip() if lines else "Unknown"
    
    print(f"\n📋 Demanda: {title}")
    print(f"   Arquivo: {filepath.name}")
    
    # Extrai projeto
    for line in lines:
        if "**Projeto:**" in line:
            project = line.replace("**Projeto:**", "").strip()
            print(f"   Projeto: {project}")
            break
    
    print()


def analyze_demand(filepath: Path, show_git=True):
    """Analisa uma demanda completa"""
    if not filepath.exists():
        print(f"❌ Arquivo não encontrado: {filepath}")
        return
    
    content = filepath.read_text(encoding="utf-8")
    demand_name = filepath.stem
    
    show_demand_summary(filepath)
    
    # Extrai outputs das seções
    def extract_section(content: str, section_name: str) -> str:
        start_marker = f"## {section_name.capitalize()}"
        end_marker = "\n## "
        
        start = content.find(start_marker)
        if start == -1:
            return ""
        
        start += len(start_marker)
        end = content.find(end_marker, start)
        if end == -1:
            end = content.find("\n---", start)
        if end == -1:
            end = len(content)
        
        return content[start:end].strip()
    
    plan_output = extract_section(content, "Plan")
    dev_output = extract_section(content, "Dev")
    qa_output = extract_section(content, "Qa")
    
    agent_outputs = {
        "Planner": plan_output,
        "Developer": dev_output,
        "QA": qa_output
    }
    
    # Git changes
    git_changes = {}
    if show_git:
        project_name = ""
        for line in content.split("\n"):
            if "**Projeto:**" in line:
                project_name = line.replace("**Projeto:**", "").strip()
                break
        
        if project_name:
            repo_path = _get_project_repo(project_name)
            branch_name = get_branch_name(filepath)
            
            if repo_path and repo_path.exists():
                git_changes = _get_git_changes(repo_path, branch_name)
    
    # Gera relatório
    report = generate_validation_report(demand_name, agent_outputs)
    print_validation_report(report)
    
    # Análise detalhada
    print("\n" + "="*70)
    print("ANÁLISE DETALHADA")
    print("="*70)
    
    for agent_name, result in report.results.items():
        print(f"\n{agent_name.upper()}")
        print("─" * 70)
        
        # Output length
        if result.output_length == 0:
            print(f"⚠️ ALERTA: Output vazio!")
        else:
            print(f"✅ Output: {result.output_length} caracteres")
        
        # Análise de conteúdo
        output_lower = agent_outputs[agent_name].lower()
        
        if agent_name.lower() == "planner":
            print("\nVerificando elementos esperados:")
            elements = {
                "Tarefas": ["tarefa", "task", "passo", "etapa"],
                "Critérios": ["critério", "criteria", "aceite", "acceptance"],
                "Tecnologias": ["tecnologia", "tech", "stack", "framework", "linguagem"],
                "Complexidade": ["baixa", "média", "alta", "complexity", "estimate"]
            }
            
            for element, keywords in elements.items():
                found = any(kw in output_lower for kw in keywords)
                status = "✅" if found else "❌"
                print(f"  {status} {element}")
        
        elif agent_name.lower() == "developer":
            print("\nVerificando elementos esperados:")
            
            code_blocks = agent_outputs[agent_name].count("```")
            print(f"  {'✅' if code_blocks > 0 else '❌'} Blocos de código: {code_blocks // 2}")
            
            has_comments = "#" in agent_outputs[agent_name] or "//" in agent_outputs[agent_name]
            print(f"  {'✅' if has_comments else '❌'} Comentários no código")
            
            has_explanation = "explicação" in output_lower or "explanation" in output_lower
            print(f"  {'✅' if has_explanation else '❌'} Explicação de decisões")
        
        elif agent_name.lower() == "qa":
            print("\nVerificando elementos esperados:")
            
            has_verdict = "✅" in agent_outputs[agent_name] or "⚠️" in agent_outputs[agent_name] or "❌" in agent_outputs[agent_name]
            has_verdict_word = any(w in output_lower for w in ["aprovado", "aprovada", "reprovado", "approved", "rejected"])
            has_result = has_verdict or has_verdict_word
            
            print(f"  {'✅' if has_result else '❌'} Veredicto final")
            
            has_bugs = any(w in output_lower for w in ["bug", "issue", "problema", "erro"])
            print(f"  {'✅' if has_bugs else '❌'} Análise de bugs/problemas")
            
            has_suggestions = any(w in output_lower for w in ["sugestão", "melhoria", "recommendation", "suggestion"])
            print(f"  {'✅' if has_suggestions else '❌'} Sugestões de melhoria")


def main():
    """Menu principal"""
    
    print("\n" + "="*70)
    print("DEBUG DOS AGENTS")
    print("="*70)
    
    # Lista demandas
    all_demands = find_demands()
    
    if not all_demands:
        print("\n❌ Nenhuma demanda encontrada")
        return
    
    # Agrupa por status
    statuses = {}
    for demand in all_demands:
        status = demand["status"]
        if status not in statuses:
            statuses[status] = []
        statuses[status].append(demand)
    
    # Exibe menu
    print("\nDemandas encontradas:")
    print()
    
    idx = 1
    demand_map = {}
    
    for status in ["in_progress", "pending", "done"]:
        if status in statuses:
            print(f"  {status.upper()}:")
            for demand in statuses[status]:
                icon = {"in_progress": "⚡", "pending": "⏳", "done": "✅"}.get(status, "")
                print(f"    {idx}. {icon} {demand['name']}")
                demand_map[idx] = demand
                idx += 1
            print()
    
    # Seleciona demanda
    try:
        choice = int(input("Escolha uma demanda (número): "))
        if choice not in demand_map:
            print("❌ Opção inválida")
            return
    except ValueError:
        print("❌ Digite um número válido")
        return
    
    selected = demand_map[choice]
    
    # Analisa
    print("\n🔍 Analisando demanda...\n")
    analyze_demand(selected["file"])


if __name__ == "__main__":
    main()
