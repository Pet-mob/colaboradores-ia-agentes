#!/usr/bin/env python3
"""
Test: Stack Detection e Database Knowledge Base
================================================

Valida:
1. Stack detection funciona corretamente para cada demanda
2. Database context está sendo injetado
3. Prompts estão sendo enriquecidos com database KB
"""

import sys
from pathlib import Path

sys.path.insert(0, ".")

from tools.stack_detector import (
    Stack,
    detect_stacks_from_demand,
    get_primary_stack,
    get_affected_stacks,
    get_stack_appropriate_context,
    get_validation_instructions,
)
from tools.database_knowledge_base import (
    get_database_context_for_developer,
    DATABASE_SCHEMA,
    DAPPER_PATTERNS,
)


def test_stack_detection():
    """Test: Stack detection por demanda"""
    print("=" * 80)
    print("TEST 1: Stack Detection")
    print("=" * 80)
    
    test_cases = [
        {
            "name": "Bug na API (Usuário/Agendamento)",
            "text": """# Demanda: Bug ao buscar agendamentos do usuário
**Projeto:** Pet.ON.Api
**Tipo:** Bug Fix

## Descrição
Usuários não conseguem visualizar seus agendamentos. O repositório
tem um problema na query SQL que busca agendamentos.
""",
            "project": "Pet.ON.Api",
            "expected_primary": Stack.BACKEND_API,
        },
        {
            "name": "Feature Frontend - Novo componente",
            "text": """# Demanda: Adicionar filtro de categoria na listagem
**Projeto:** PetShop.WebApp
**Tipo:** Feature

## Descrição
Adicionar componente de filtro para categorias de serviço na página home.
Deve ser integrado com Pinia store.
""",
            "project": "PetShop.WebApp",
            "expected_primary": Stack.FRONTEND_WEBAPP,
        },
        {
            "name": "Feature Mobile - Novo agendamento",
            "text": """# Demanda: Implementar fluxo de agendamento mobile
**Projeto:** Pet.ON.App
**Tipo:** Feature

## Descrição
Criar nova tela de agendamento para mobile com múltiplos passos.
Integrar com API de agendamentos.
""",
            "project": "Pet.ON.App",
            "expected_primary": Stack.MOBILE_APP,
        },
    ]
    
    for test in test_cases:
        print(f"\n📋 {test['name']}")
        
        scores = detect_stacks_from_demand(test["text"], test["project"])
        primary = get_primary_stack(scores)
        
        print(f"   Scores: {scores}")
        print(f"   Primary: {primary.value}")
        print(f"   Expected: {test['expected_primary'].value}")
        
        if primary == test["expected_primary"]:
            print(f"   ✅ PASSOU")
        else:
            print(f"   ❌ FALHOU - esperava {test['expected_primary'].value}")
    
    print("\n" + "=" * 80)


def test_database_context():
    """Test: Database context injection"""
    print("\nTEST 2: Database Context Injection")
    print("=" * 80)
    
    context = get_database_context_for_developer()
    
    # Validar que contém padrões esperados
    checks = [
        ("Dapper" in context, "Menciona Dapper"),
        ("Entity Framework" not in context, "NÃO menciona Entity Framework"),
        ("QueryAsync" in context, "Contém exemplo QueryAsync"),
        ("SqlRetryHelper" in context, "Menciona SqlRetryHelper"),
        ("IDbConnection" in context, "Menciona IDbConnection"),
        ("FIELD_MAPPINGS" in context, "Contém field mappings"),
    ]
    
    for check, description in checks:
        status = "✅" if check else "❌"
        print(f"{status} {description}")
    
    print("\n" + "=" * 80)


def test_schema_completeness():
    """Test: Schema possui todas as tabelas necessárias"""
    print("\nTEST 3: Schema Completeness")
    print("=" * 80)
    
    required_tables = [
        "Usuario",
        "Animal",
        "Empresa",
        "Servico",
        "Agendamento",
        "Endereco",
    ]
    
    print(f"\nTabelas no schema: {len(DATABASE_SCHEMA)}")
    
    for table in required_tables:
        if table in DATABASE_SCHEMA:
            print(f"✅ {table}")
            schema = DATABASE_SCHEMA[table]
            print(f"   - Colunas: {len(schema['columns'])}")
            print(f"   - Relacionamentos: {len(schema.get('relationships', {}))}")
        else:
            print(f"❌ {table} (FALTANDO!)")
    
    print("\n" + "=" * 80)


def test_dapper_patterns():
    """Test: Dapper patterns existem"""
    print("\nTEST 4: Dapper Patterns")
    print("=" * 80)
    
    patterns = [
        "basic_query",
        "query_with_parameters",
        "insert",
        "update",
        "transaction",
        "retry_pattern",
    ]
    
    for pattern in patterns:
        if pattern in DAPPER_PATTERNS:
            print(f"✅ {pattern}")
        else:
            print(f"❌ {pattern} (FALTANDO!)")
    
    print("\n" + "=" * 80)


def test_stack_validation_message():
    """Test: Mensagens de validação de stack"""
    print("\nTEST 5: Stack Validation Messages")
    print("=" * 80)
    
    # Test single stack
    validation_single = get_validation_instructions([Stack.BACKEND_API])
    print("\n📌 Single Stack Validation:")
    print(validation_single[:200] + "...")
    
    # Test multiple stacks
    validation_multi = get_validation_instructions([Stack.BACKEND_API, Stack.FRONTEND_WEBAPP])
    print("\n📌 Multiple Stack Validation:")
    print(validation_multi[:200] + "...")
    
    print("\n" + "=" * 80)


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "🧪 STACK DETECTION & DATABASE KB TESTS" + " " * 20 + "║")
    print("╚" + "=" * 78 + "╝")
    
    test_stack_detection()
    test_database_context()
    test_schema_completeness()
    test_dapper_patterns()
    test_stack_validation_message()
    
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 25 + "✅ TODOS OS TESTES COMPLETADOS" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝\n")


if __name__ == "__main__":
    main()
