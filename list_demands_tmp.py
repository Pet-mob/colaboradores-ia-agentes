from tasks.queue_manager import list_demands

demands = list_demands('in_progress')
print(f'Demandas em progresso: {len(demands)}')
for d in demands[:5]:
    print(f'  ✓ {d["name"]}')
