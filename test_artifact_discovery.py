#!/usr/bin/env python3
"""
Test: Artifact Discovery + Clarification System
===============================================

Valida:
1. Artifact discovery encontra entidades/repos/services existentes
2. Clarification system detecta ambiguidades
3. Reuse suggestions aparecem corretamente
"""

import sys
from pathlib import Path

sys.path.insert(0, ".")

from tools.artifact_discoverer import ArtifactDiscoverer
from tools.clarification_system import (
    ClarificationGenerator,
    extract_entity_names_from_demand,
)


def test_artifact_discovery():
    """Test: Descobrir artifacts existentes"""
    print("=" * 80)
    print("TEST 1: Artifact Discovery")
    print("=" * 80)
    
    discoverer = ArtifactDiscoverer()
    inventory = discoverer.get_full_inventory()
    
    print(f"\n✅ Entidades descobertas: {len(inventory['entities'])}")
    for name in sorted(inventory['entities'].keys()):
        details = inventory['entities'][name]
        props = len(details.get('properties', []))
        methods = len(details.get('methods', []))
        print(f"   - {name:<20} ({props} props, {methods} métodos)")
    
    print(f"\n✅ Repositories descobertos: {len(inventory['repositories'])}")
    for name in sorted(inventory['repositories'].keys()):
        methods = len(inventory['repositories'][name].get('methods', []))
        print(f"   - {name:<30} ({methods} métodos)")
    
    expected_entities = ["Usuario", "Animal", "Empresa", "Agendamento"]
    missing = [e for e in expected_entities if e not in inventory['entities']]
    
    if not missing:
        print(f"\n✅ Todas as entidades esperadas encontradas!")
    else:
        print(f"\n❌ Entidades faltando: {missing}")
    
    print("\n" + "=" * 80)


def test_entity_name_extraction():
    """Test: Extrair nomes de entidades da demanda"""
    print("\nTEST 2: Entity Name Extraction")
    print("=" * 80)
    
    test_cases = [
        {
            "name": "Selo de Qualidade (menciona Empresa implicitamente)",
            "text": """# Demanda: Selo de Qualidade
Implementar Selo de Qualidade para lojas. 
Cada empresa pode ter um selo de certificação.""",
            "expected_contains": ["Selo", "Empresa", "Qualidade"],
        },
        {
            "name": "Novo status de agendamento",
            "text": """# Demanda: Status de Agendamento
Adicionar novo status 'EmAtendimento' à entidade Agendamento.""",
            "expected_contains": ["Status", "Agendamento"],
        },
    ]
    
    for test in test_cases:
        print(f"\n📋 {test['name']}")
        entities = extract_entity_names_from_demand(test['text'])
        print(f"   Entidades encontradas: {entities}")
        
        for expected in test['expected_contains']:
            if any(expected.lower() in e.lower() for e in entities):
                print(f"   ✅ {expected}")
            else:
                print(f"   ⚠️ {expected} não encontrado")
    
    print("\n" + "=" * 80)


def test_clarification_generation():
    """Test: Gerar clarification questions"""
    print("\nTEST 3: Clarification Generation")
    print("=" * 80)
    
    demand_text = """# Demanda: Implementar Selo de Qualidade
**Projeto:** Pet.ON.Api

Cada empresa (PetShop) precisa de um Selo de Qualidade que indica
se está certificada. O selo tem validade e critérios."""
    
    entity_names = extract_entity_names_from_demand(demand_text)
    print(f"\n📋 Demanda: Selo de Qualidade da Loja")
    print(f"Entidades mencionadas: {entity_names}")
    
    gen = ClarificationGenerator()
    
    # Verifica se precisa clarificação
    should_ask = gen.should_ask_clarifications(entity_names)
    print(f"\n❓ Precisa clarificação? {should_ask}")
    
    if should_ask:
        # Gera prompt de clarificação
        prompt = gen.generate_clarification_prompt_for_planner(demand_text, entity_names)
        print("\n✅ Prompt de Clarificação:")
        print("-" * 80)
        print(prompt[:500] + "...")
    
    # Reuse suggestions
    print("\n✅ Reuse Suggestions:")
    reuse = gen.generate_reuse_suggestions(demand_text)
    print(f"   Entities to extend: {reuse['entities_to_extend']}")
    print(f"   Repositories to update: {reuse['repositories_to_update']}")
    
    if "Empresa" in reuse['entities_to_extend']:
        print(f"   ✅ Empresa foi sugerida para extensão (correto!)")
    
    print("\n" + "=" * 80)


def test_entity_relationship_discovery():
    """Test: Descobrir artifacts relacionados"""
    print("\nTEST 4: Related Artifacts Discovery")
    print("=" * 80)
    
    discoverer = ArtifactDiscoverer()
    
    # Testa com Empresa
    print("\n📋 Artifacts relacionados a 'Empresa':")
    related = discoverer.get_related_artifacts("Empresa")
    
    print(f"   Entity: {related['entity'].get('description', 'N/A')[:80]}...")
    print(f"   Repository: {'✅' if related['repository'] else '❌'}")
    print(f"   DTOs: {len(related['dtos'])} encontrados")
    if related['dtos']:
        for dto_name in list(related['dtos'].keys())[:3]:
            print(f"      - {dto_name}")
    
    print("\n" + "=" * 80)


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "🔍 ARTIFACT DISCOVERY + CLARIFICATION TESTS" + " " * 21 + "║")
    print("╚" + "=" * 78 + "╝")
    
    test_artifact_discovery()
    test_entity_name_extraction()
    test_clarification_generation()
    test_entity_relationship_discovery()
    
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 25 + "✅ TODOS OS TESTES COMPLETADOS" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝\n")


if __name__ == "__main__":
    main()
