#!/usr/bin/env python3
"""
Teste COMPLETO do pipeline: generate → extract → create files → commit
"""
from pathlib import Path
from agents.orchestrator import run_ai_team
from tasks.queue_manager import move_to_in_progress, move_to_done

print("=" * 80)
print("TESTE COMPLETO DO PIPELINE DE MATERIALIZAÇÃO DE CÓDIGO")
print("=" * 80)

# Usar a demanda mais simples da fila em in_progress
demand_file_in_progress = Path("demands/in_progress/013-sistema-confirmacao-servicos.md")

if not demand_file_in_progress.exists():
    print(f"\n[ERROR] Arquivo {demand_file_in_progress} não existe")
    print("Demandas disponíveis:")
    for d in Path("demands").rglob("*.md"):
        print(f"  - {d.relative_to('demands')}")
    exit(1)

print(f"\n[1] Processando demanda que já está em 'in_progress'...")
demand_file = demand_file_in_progress

# Backup path before running
print(f"\n[2] Iniciando execução da demanda...")
print(f"    - Planner Agent: Gerar plano")
print(f"    - Developer Agent: Gerar código COM '# File:' headers")
print(f"    - Code Generator: Extrair blocos de código")
print(f"    - File Creator: Criar arquivos nos repositórios")
print(f"    - Git Manager: Fazer commit com alterações reais")
print()

try:
    result = run_ai_team(demand_file)
    print(f"\n[3] Resultado da execução:")
    print(f"{result[:500]}..." if len(result) > 500 else result)
    
    print(f"\n[4] Movendo para 'done'...")
    move_to_done(demand_file)
    
    print(f"\n{'=' * 80}")
    print("✅ PIPELINE COMPLETO EXECUTADO COM SUCESSO!")
    print(f"{'=' * 80}\n")
    print("Próximos passos:")
    print("  1. Verifique os commits no repositório local (Pet.ON.Api, etc)")
    print("  2. Veja se os arquivos foram criados corretamente")
    print("  3. Valide se o commit referencia a demanda (feat(012-...) ...)")
    
except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
    exit(1)
