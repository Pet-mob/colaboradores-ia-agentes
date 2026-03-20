"""
Script para processar a próxima demanda pendente
"""

import sys
from pathlib import Path
from tasks.queue_manager import get_next_pending, move_to_in_progress
from agents.orchestrator import run_ai_team

demand_file = get_next_pending()

if not demand_file:
    print("❌ Nenhuma demanda pendente encontrada!")
    sys.exit(1)

print(f"🎯 Processando: {demand_file.name}\n")

# Move para in_progress
demand_file = move_to_in_progress(demand_file)

try:
    # Executa os agents
    result = run_ai_team(demand_file)
    print(f"\n✅ Demanda processada com sucesso!")
except Exception as e:
    print(f"\n❌ Erro: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
