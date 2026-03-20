"""
Script para testar o pipeline completo de materializacao de código
"""
from pathlib import Path
from agents.orchestrator import run_ai_team

# Processa a demanda que ja estava em andamento
demand_file = Path("demands/in_progress/044-bug-dados-incorretos.md")

if not demand_file.exists():
    print(f"[ERROR] Arquivo nao encontrado: {demand_file}")
    exit(1)

print(f"[TEST] Testando pipeline com: {demand_file.name}\n")
print("=" * 70)

try:
    result = run_ai_team(demand_file)
    print("\n" + "=" * 70)
    print("[OK] Pipeline executado com sucesso!")
    print(f"\nResultado QA:\n{result[:300]}...")
except Exception as e:
    print("\n" + "=" * 70)
    print(f"[ERROR] Erro: {e}")
    import traceback
    traceback.print_exc()
