#!/usr/bin/env python3
"""
Test: Processo simples de uma demanda para validar branches
"""

from pathlib import Path
from agents.orchestrator import run_ai_team

# Pega primeira demanda em in_progress
demands_dir = Path("demands/in_progress")
demands = sorted([f for f in demands_dir.glob("*.md")])

if not demands:
    print("❌ Nenhuma demanda encontrada em in_progress/")
    exit(1)

demand_file = demands[0]

print(f"\n{'='*80}")
print(f"PROCESSANDO DEMANDA: {demand_file.name}")
print(f"{'='*80}\n")

try:
    run_ai_team(demand_file)
    print("\n✅ DEMANDA PROCESSADA COM SUCESSO!")
except Exception as e:
    print(f"\n❌ ERRO: {e}")
    import traceback
    traceback.print_exc()
