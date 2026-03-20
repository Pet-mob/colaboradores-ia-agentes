#!/usr/bin/env python
"""
Script de validação dos agents
Use isto para testar e debugar a execução dos agents
"""

import sys
from pathlib import Path
from tools.agents_validator import (
    validate_agent_output,
    generate_validation_report,
    print_validation_report
)


def validate_single_output(agent_name: str, output_file: Path = None):
    """Valida o output de um único agent"""
    print(f"\n🔍 Validando {agent_name}...\n")
    
    if output_file and output_file.exists():
        output = output_file.read_text(encoding="utf-8")
    else:
        # Pede input do usuário
        print(f"Cole o output do {agent_name} (termine com Ctrl+D ou Ctrl+Z):")
        try:
            output = sys.stdin.read()
        except EOFError:
            output = sys.stdin.getvalue()
    
    result = validate_agent_output(agent_name, output)
    
    print(f"Resultado da validação:")
    print(f"  Score: {result.quality_score:.0f}/100")
    print(f"  Tamanho do output: {result.output_length} caracteres")
    print(f"  Válido: {'✅ Sim' if result.is_valid else '❌ Não'}")
    
    if result.issues:
        print(f"\nProblemas encontrados:")
        for issue in result.issues:
            print(f"  ⚠️ {issue}")
    else:
        print(f"\n✅ Nenhum problema detectado")
    
    return result


def validate_demand_file(demand_file: Path):
    """Valida os outputs de uma demanda a partir de um arquivo .md"""
    if not demand_file.exists():
        print(f"❌ Arquivo não encontrado: {demand_file}")
        return
    
    content = demand_file.read_text(encoding="utf-8")
    
    # Extrai os outputs de cada seção
    def extract_section(content: str, section: str) -> str:
        patterns = [
            f"## {section.capitalize()}",
            f"### {section.capitalize()}",
            f"# {section.capitalize()}"
        ]
        
        for pattern in patterns:
            if pattern in content:
                start = content.find(pattern)
                # Encontra o próximo seção
                next_section = content.find("\n##", start + len(pattern))
                if next_section == -1:
                    next_section = len(content)
                return content[start:next_section].strip()
        
        return ""
    
    plan_output = extract_section(content, "plan")
    dev_output = extract_section(content, "dev")
    qa_output = extract_section(content, "qa")
    
    demand_name = demand_file.stem
    
    agent_outputs = {
        "Planner": plan_output,
        "Developer": dev_output,
        "QA": qa_output
    }
    
    # Gera relatório
    report = generate_validation_report(demand_name, agent_outputs)
    print_validation_report(report)


def interactive_menu():
    """Menu interativo para validação"""
    while True:
        print("\n" + "="*70)
        print("VALIDADOR DE AGENTS - Menu")
        print("="*70)
        print("""
1. Validar output individual de um agent
2. Validar demanda completa (arquivo .md)
3. Testar validador com dados de exemplo
4. Sair
        """)
        
        choice = input("Escolha uma opção (1-4): ").strip()
        
        if choice == "1":
            agent_name = input("\nNome do agent (Planner/Developer/QA): ").strip()
            validate_single_output(agent_name)
        
        elif choice == "2":
            filepath = input("\nCaminho do arquivo de demanda: ").strip()
            validate_demand_file(Path(filepath))
        
        elif choice == "3":
            print("\n🧪 Testando com dados de exemplo...\n")
            
            test_outputs = {
                "Planner": """
# Plano Técnico

## Tarefas
1. Configurar banco de dados
   - Critério de aceite: Schema criado
2. Criar API REST
   - Critério de aceite: Endpoints retornam JSON válido

## Tecnologias
- .NET 8.0
- Entity Framework Core
- PostgreSQL

## Complexidade
Alta
                """,
                "Developer": """
# Implementação

## Backend (.NET)

```csharp
[ApiController]
[Route("api/[controller]")]
public class PetsController : ControllerBase {
    [HttpGet]
    public async Task<IActionResult> GetPets() {
        return Ok(await _service.GetAllAsync());
    }
}
```

## Notas
- Implementado padrão Repository
- Injeção de dependência configurada
                """,
                "QA": """
# Relatório de Qualidade

## Bugs Encontrados
1. Validação de entrada faltando
2. Tratamento de erro incompleto

## Sugestões de Melhoria
- Adicionar logging
- Criar testes unitários

## Veredicto Final
⚠️ Aprovado com ressalvas
                """
            }
            
            report = generate_validation_report("Teste Example", test_outputs)
            print_validation_report(report)
        
        elif choice == "4":
            print("\nSaindo...\n")
            break
        
        else:
            print("\n❌ Opção inválida")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Modo linha de comando: validar arquivo
        filepath = Path(sys.argv[1])
        validate_demand_file(filepath)
    else:
        # Modo interativo
        interactive_menu()
