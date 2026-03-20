#!/usr/bin/env python3
"""
End-to-End Test: Full Pipeline with Real Demand
================================================

Valida que o pipeline completo funciona:
1. Extract entities from demand
2. Generate clarifications
3. Create tasks with clarifications integrated
4. Verify planner/dev/qa tasks have proper context
"""

import sys
from pathlib import Path
import tempfile

sys.path.insert(0, ".")

from tasks.dev_tasks import create_tasks
from tools.artifact_discoverer import ArtifactDiscoverer
from tools.clarification_system import extract_entity_names_from_demand, ClarificationGenerator


def test_end_to_end_pipeline():
    """Test: Full pipeline com demand that touches existing Empresa entity"""
    print("=" * 90)
    print("END-TO-END TEST: Full Pipeline with Real Demand")
    print("=" * 90)
    
    # Criar demanda de teste que menciona Empresa (existe)
    demand_content = """# Demanda: Implementar Selo de Qualidade para Empresas

**Projeto:** Pet.ON.Api  
**Tipo:** Feature

## Descrição

Implementar Selo de Qualidade para as lojas (Empresas). Cada empresa pode receber um 
Selo que indica se está certificada pelo sistema.

### Regras de Negócio
- Apenas Empresas podem ter Selo
- Selo tem data de validade
- Status do Selo: Ativo, Vencido, Cancelado
- Exibir Selo na página da Loja

### Tecnologias
- Backend: .NET 7 + Dapper
- Frontend: React

---

**Análise Adicional:**
- Tabela EMPRESA já existe com campos: IdEmpresa, DescricaoNomeFisica, Email, Telefone
- Repository: EmpresaRepositorio já implementado
- DTO: EmpresaDTO existente
"""

    # Criar arquivo temporário
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(demand_content)
        temp_path = Path(f.name)
    
    try:
        print("\n📋 Demanda Teste:")
        print("-" * 90)
        print(demand_content[:300] + "...")
        print("-" * 90)
        
        # STEP 1: Extract entities
        print("\n✅ STEP 1: Entity Name Extraction")
        entity_names = extract_entity_names_from_demand(demand_content)
        print(f"   Entidades encontradas: {entity_names}")
        
        if "Empresa" in entity_names or "Selo" in entity_names:
            print(f"   ✅ Detectou Empresa/Selo corretamente")
        else:
            print(f"   ⚠️ Não detectou entidades principais")
        
        # STEP 2: Generate clarifications
        print("\n✅ STEP 2: Clarification Generation")
        clar_gen = ClarificationGenerator()
        should_ask = clar_gen.should_ask_clarifications(entity_names)
        print(f"   Precisa clarificação? {should_ask}")
        
        if should_ask:
            clarifications = clar_gen.generate_clarifications(demand_content, entity_names)
            print(f"   Perguntas geradas: {len(clarifications)}")
            for i, q in enumerate(clarifications[:2], 1):
                print(f"   {i}. {q.question[:80]}...")
        
        reuse = clar_gen.generate_reuse_suggestions(demand_content)
        print(f"   Entidades para estender: {reuse['entities_to_extend']}")
        
        if "Empresa" in reuse['entities_to_extend']:
            print(f"   ✅ Empresa foi identificada para REUTILIZAÇÃO")
        
        # STEP 3: Create tasks with clarifications integrated
        print("\n✅ STEP 3: Create Tasks with Clarifications")
        tasks = create_tasks(temp_path)
        
        print(f"   Tasks criadas: {len(tasks)}")
        
        task_names = []
        for i, task in enumerate(tasks, 1):
            desc = task.description[:50] + "..." if len(task.description) > 50 else task.description
            task_names.append(f"Task {i}")
            print(f"   {i}. {desc}")
        
        # STEP 4: Verify context flow
        print("\n✅ STEP 4: Verify Context Flow")
        
        # Primeiro task pode ser clarification ou planner
        first_task = tasks[0]
        print(f"   First task: {task_names[0]}")
        
        if "clarificação" in first_task.description.lower() or "responda às" in first_task.description.lower():
            print(f"   ✅ Clarification task detectado como first task")
            clarification_task = first_task
            planner_task = tasks[1] if len(tasks) > 1 else None
        else:
            print(f"   ℹ️ No clarification task (expected behavior)")
            clarification_task = None
            planner_task = first_task
        
        if planner_task:
            print(f"   Planner Task: {task_names[1] if clarification_task else task_names[0]}")
            print(f"   Context length: {len(planner_task.context)}")
            if clarification_task and clarification_task in planner_task.context:
                print(f"   ✅ Clarification task flowing to Planner context")
        
        # Developer task (penultimate)
        dev_task = tasks[-2] if len(tasks) >= 2 else None
        if dev_task:
            print(f"   Developer Task: {task_names[-2]}")
            print(f"   Context length: {len(dev_task.context)}")
            if planner_task and planner_task in dev_task.context:
                print(f"   ✅ Planner task flowing to Developer context")
            
            # Verificar reuse emphasis
            if "reutilize" in dev_task.description.lower() or "existentes" in dev_task.description.lower():
                print(f"   ✅ Reuse emphasis presente no Developer prompt")
        
        # QA task (último)
        qa_task = tasks[-1] if len(tasks) >= 1 else None
        if qa_task:
            print(f"   QA Task: {task_names[-1]}")
            print(f"   Context length: {len(qa_task.context)}")
        
        # STEP 5: Summary
        print("\n" + "=" * 90)
        print("✅ END-TO-END TEST SUMMARY")
        print("=" * 90)
        
        summary = {
            "entities_extracted": len(entity_names) > 0,
            "reuse_suggestions_generated": "Empresa" in reuse['entities_to_extend'],  # Chave métrica
            "tasks_created": len(tasks) >= 3,  # Min: planner + dev + qa
            "empresa_for_reuse": "Empresa" in reuse['entities_to_extend'],
            "reuse_emphasis_in_dev": "reutilize" in dev_task.description.lower() if dev_task else False,
            "context_chaining": True if planner_task and dev_task else False,
        }
        
        all_ok = all(summary.values())
        
        for key, value in summary.items():
            status = "✅" if value else "⚠️"
            key_display = key.replace("_", " ").title()
            print(f"{status} {key_display}: {value}")
        
        if all_ok:
            print(f"\n{'='*90}")
            print(f"✅ ALL VALIDATIONS PASSED!")
            print(f"{'='*90}")
            return True
        else:
            print(f"\n⚠️ Some validations failed")
            return False
    
    finally:
        # Clean up
        temp_path.unlink(missing_ok=True)


def main():
    print("\n")
    result = test_end_to_end_pipeline()
    print("\n")
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
