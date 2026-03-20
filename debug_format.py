#!/usr/bin/env python3
"""
Analisar formato das demandas para debugar code_generator.py
"""
from pathlib import Path
import re

# Lê um arquivo de demanda já processada
demand = Path('demands/done/044-bug-dados-incorretos.md').read_text(encoding='utf-8')

print("=== Análise da Demanda ===\n")

# Procura por padrão "File:" 
file_patterns = re.findall(r'^#+\s*File:\s*(.+?)$', demand, re.MULTILINE)
print(f"[1] Padrão '# File:' encontrado: {len(file_patterns)} vez(es)")
for fp in file_patterns[:3]:
    print(f"    - {fp}")

# Procura por padrão alternativo "file:"
file_patterns2 = re.findall(r'^#+\s+file:\s*(.+?)$', demand, re.MULTILINE | re.IGNORECASE)
print(f"\n[2] Padrão '# file:' (case-insensitive) encontrado: {len(file_patterns2)} vez(es)")
for fp in file_patterns2[:3]:
    print(f"    - {fp}")

# Conta blocos de código
code_blocks = re.findall(r'^```', demand, re.MULTILINE)
print(f"\n[3] Blocos de código encontrados: {len(code_blocks)}")

# Amostra de um trecho
idx = demand.find('## Desenvolvimento')
if idx == -1:
    idx = demand.find('## 🚀 Desenvolvimento')
if idx == -1:
    idx = demand.find('Desenvolvimento')
    
if idx > 0:
    amostra = demand[idx:idx+300]
    print(f"\n[4] Amostra do texto em torno de 'Desenvolvimento':\n{amostra}")
else:
    print("\n[4] Seção 'Desenvolvimento' não encontrada")
