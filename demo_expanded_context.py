"""
Demonstrador: Como os Agents AGORA recebem contexto super detalhado
"""

import sys
from tools.context_enricher import get_context_enricher

# Fix encoding para Windows
if sys.stdout.encoding == 'cp1252':
    sys.stdout.reconfigure(encoding='utf-8')

def demo_expanded_context():
    enricher = get_context_enricher()
    
    print("\n" + "="*80)
    print("[DEMO] CONTEXTO EXPANDIDO DOS AGENTS")
    print("="*80)
    
    # Demonstra contexto do Planner
    print("\n" + "─"*80)
    print("1️⃣  CONTEXTO PARA PLANNER AGENT")
    print("─"*80)
    
    planner_context = enricher.enrich_planner_prompt(
        project_name="pet.on.api",
        demand_type="feature",
        title="Adicionar suporte a fotos de capa para petshops",
        description="As petshops precisam de fotos de capa que apareçam na listagem e detalhes"
    )
    
    # Mostrar primeiras 2000 chars
    print(planner_context[:2000])
    print(f"\n... [Total: {len(planner_context)} caracteres]")
    
    # Demonstra contexto do Developer
    print("\n" + "─"*80)
    print("2️⃣  CONTEXTO PARA DEVELOPER AGENT")
    print("─"*80)
    
    developer_context = enricher.enrich_developer_prompt(
        project_name="pet.on.api",
        title="Implementar upload de fotos para petshops",
        description="Feature para upload de fotos",
        plan="Plano do Planner aqui..."
    )
    
    print(developer_context[:2500])
    print(f"\n... [Total: {len(developer_context)} caracteres]")
    
    # Demonstra contexto do QA
    print("\n" + "─"*80)
    print("3️⃣  CONTEXTO PARA QA AGENT")
    print("─"*80)
    
    qa_context = enricher.enrich_qa_prompt(
        project_name="pet.on.api",
        title="Validar qualidade de feature de fotos",
        plan="Plano aqui...",
        implementation="Implementação aqui..."
    )
    
    print(qa_context[:2500])
    print(f"\n... [Total: {len(qa_context)} caracteres]")
    
    # Resumo de tamanhos
    print("\n" + "="*80)
    print("📊 RESUMO: QUANTIDADE DE CONTEXTO INJETADA")
    print("="*80)
    
    print(f"""
Planner Context:   {len(planner_context):,} caracteres
Developer Context: {len(developer_context):,} caracteres  
QA Context:        {len(qa_context):,} caracteres

MELHORIA: Antes tínhamos ~100-500 chars por agente
          Agora têm ~8,000-15,000 chars com contexto super detalhado!

Isso inclui:
  ✅ Estrutura completa de pastas
  ✅ Endpoints e APIs
  ✅ Modelos de dados
  ✅ Componentes disponíveis
  ✅ Padrões de código
  ✅ Telas e navegação
  ✅ Regras de negócio
  ✅ Validações
  ✅ Formatos de dados
  ✅ Ambientes (dev, staging, prod)
""")


if __name__ == "__main__":
    demo_expanded_context()
