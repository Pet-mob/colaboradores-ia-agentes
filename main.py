from config.settings import GROQ_API_KEY
from agents.orchestrator import run_ai_team
from tasks.queue_manager import (
    add_demand, list_demands, get_next_pending,
    move_to_in_progress, move_to_done,
    PROJECTS, DEMAND_TYPES
)


def show_queue():
    demands = list_demands()
    if not demands:
        print("\n  Fila vazia.")
        return
    icons = {"pending": "⏳ pending", "in_progress": "⚡ working", "done": "✅ done"}
    print(f"\n{'Status':<14} {'Arquivo'}")
    print("-" * 70)
    for d in demands:
        print(f"{icons.get(d['status'], d['status']):<14} {d['name']}")
    print()


def prompt_add():
    print("\n--- Nova Demanda ---")

    print("Projetos disponíveis:")
    for i, p in enumerate(PROJECTS, 1):
        print(f"  {i}. {p}")
    project = PROJECTS[int(input("Projeto (número): ").strip()) - 1]

    print("\nTipos:")
    for i, t in enumerate(DEMAND_TYPES, 1):
        print(f"  {i}. {t}")
    demand_type = DEMAND_TYPES[int(input("Tipo (número): ").strip()) - 1]

    title = input("\nTítulo da demanda: ").strip()
    description = input("Descrição detalhada: ").strip()

    filepath = add_demand(title, description, project, demand_type)
    print(f"\n✅ Arquivo criado: {filepath}")


def process_in_progress():
    in_progress = list_demands(status="in_progress")
    if not in_progress:
        print("\n  Nenhuma demanda em andamento.")
        return

    print("\n--- Demandas em andamento ---")
    for i, d in enumerate(in_progress, 1):
        print(f"  {i}. {d['name']}")

    choice = input("\nEscolha o número para processar (0 para cancelar): ").strip()
    if choice == "0" or not choice.isdigit():
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(in_progress):
        print("  Opção inválida.")
        return

    filepath = in_progress[idx]["file"]
    print(f"\n🚀 Processando: {filepath.name}")
    run_ai_team(filepath)
    move_to_done(filepath)
    print(f"\n✅ Concluído! Arquivo em: demands/done/{filepath.name}")


def process_next():
    filepath = get_next_pending()
    if not filepath:
        print("\n  Nenhuma demanda pendente.")
        return

    print(f"\n🚀 Iniciando: {filepath.name}")
    filepath = move_to_in_progress(filepath)
    run_ai_team(filepath)
    move_to_done(filepath)
    print(f"\n✅ Concluído! Arquivo em: demands/done/{filepath.name}")


if __name__ == "__main__":
    print("\n=== Petmob AI Agents ===")

    while True:
        print("\n1. Ver fila")
        print("2. Adicionar demanda")
        print("3. Processar próxima demanda")
        print("4. Processar todas as pendentes")
        print("5. Processar demanda em andamento")
        print("0. Sair")

        choice = input("\nEscolha: ").strip()

        if choice == "1":
            show_queue()
        elif choice == "2":
            prompt_add()
        elif choice == "3":
            process_next()
        elif choice == "4":
            pending = list_demands(status="pending")
            if not pending:
                print("\n  Nenhuma demanda pendente.")
            else:
                print(f"\n  Processando {len(pending)} demanda(s)...")
                while get_next_pending():
                    process_next()
                print("\n✅ Todas as demandas foram processadas.")
        elif choice == "5":
            process_in_progress()
        elif choice == "0":
            print("Até logo!")
            break
        else:
            print("  Opção inválida.")
