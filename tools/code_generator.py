"""
Extrai código gerado pela Developer Agent e cria arquivos reais no repositório.
"""

import re
from pathlib import Path
from typing import List, Tuple
import json


def extract_code_blocks(developer_output: str) -> List[Tuple[str, str, str]]:
    """
    Extrai blocos de código da output do Developer Agent.
    
    Suporta múltiplos padrões:
    1. # File: path/to/file.ext
    2. ## File: path/to/file.ext  
    3. ```language\ncode\n```
    4. Padrões sem File header (fallback para nomes genéricos)
    
    Returns:
        Lista de tuplas (filepath, language, code)
    """
    results = []
    lines = developer_output.split('\n')
    
    current_file = None
    current_lang = None
    code_block = []
    in_code = False
    block_counter = 0  # Contador para fallback names
    
    for i, line in enumerate(lines):
        # Detecta header de arquivo (múltiplos padrões)
        file_match = re.match(r'^#+\s*File:\s*(.+?)(?:\s*--|$)', line.strip(), re.IGNORECASE)
        if file_match:
            # Se tem um bloco anterior, salva
            if code_block and current_file:
                results.append((current_file, current_lang or "txt", '\n'.join(code_block)))
                code_block = []
                in_code = False
            current_file = file_match.group(1).strip()
            current_lang = None
            continue
        
        # Detecta início de bloco de código
        if line.strip().startswith('```'):
            if not in_code:
                # Início do bloco
                in_code = True
                lang_part = line.strip()[3:].strip()
                current_lang = lang_part if lang_part else "txt"
                code_block = []
                
                # Se não houver arquivo anterior, cria um genérico
                if not current_file:
                    block_counter += 1
                    # Tenta adivinhar a extensão pela linguagem
                    ext_map = {
                        'csharp': 'cs', 'c#': 'cs',
                        'javascript': 'js', 'typescript': 'ts',
                        'python': 'py', 'sql': 'sql',
                        'html': 'html', 'css': 'css',
                        'json': 'json', 'xml': 'xml',
                        'java': 'java', 'go': 'go',
                        'rust': 'rs',
                    }
                    ext = ext_map.get(lang_part.lower(), 'txt')
                    current_file = f"generated_file_{block_counter}.{ext}"
            else:
                # Fim do bloco
                in_code = False
                if code_block and current_file:
                    results.append((current_file, current_lang or "txt", '\n'.join(code_block)))
                    code_block = []
                current_lang = None
                current_file = None  # Reset para próximo bloco
            continue
        
        # Se estamos dentro de um bloco, adiciona a linha
        if in_code:
            code_block.append(line)
    
    # Se sobrou um bloco no final
    if code_block and current_file and not in_code:
        results.append((current_file, current_lang or "txt", '\n'.join(code_block)))
    
    return results


def create_project_files(
    project_repo: Path,
    code_blocks: List[Tuple[str, str, str]],
    project_type: str = "dotnet"
) -> List[Path]:
    """
    Cria os arquivos de código no repositório do projeto.
    
    Args:
        project_repo: Caminho do repositório local do projeto
        code_blocks: Lista de (filepath, language, code)
        project_type: "dotnet", "vue", "react-native"
    
    Returns:
        Lista de caminhos dos arquivos criados
    """
    created_files = []
    
    for filepath, language, code in code_blocks:
        # Normaliza o caminho
        full_path = project_repo / filepath
        
        # Cria diretório pai se não existir
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Escreve o arquivo
        try:
            full_path.write_text(code, encoding="utf-8")
            created_files.append(full_path)
            print(f"✅ Arquivo criado: {filepath}")
        except Exception as e:
            print(f"❌ Erro ao criar {filepath}: {e}")
    
    return created_files


def organize_code_by_stack(
    developer_output: str,
    project_type: str
) -> dict:
    """
    Organiza o código gerado por tipo de projeto.
    
    Retorna um dicionário com:
    {
        "models": [code_blocks],
        "controllers": [code_blocks],
        "services": [code_blocks],
        "repositories": [code_blocks],
        "components": [code_blocks],
        "utils": [code_blocks]
    }
    """
    organized = {
        "models": [],
        "controllers": [],
        "services": [],
        "repositories": [],
        "components": [],
        "utils": [],
        "other": []
    }
    
    blocks = extract_code_blocks(developer_output)
    
    for filepath, lang, code in blocks:
        filepath_lower = filepath.lower()
        
        # Categoriza por tipo de arquivo
        if any(x in filepath_lower for x in ["model", "entity", "domain"]):
            organized["models"].append((filepath, lang, code))
        elif any(x in filepath_lower for x in ["controller", "api"]):
            organized["controllers"].append((filepath, lang, code))
        elif any(x in filepath_lower for x in ["service", "use"]):
            organized["services"].append((filepath, lang, code))
        elif "repository" in filepath_lower or "repo" in filepath_lower:
            organized["repositories"].append((filepath, lang, code))
        elif any(x in filepath_lower for x in ["component", "vue", "app", "screen"]):
            organized["components"].append((filepath, lang, code))
        elif any(x in filepath_lower for x in ["util", "helper", "constant"]):
            organized["utils"].append((filepath, lang, code))
        else:
            organized["other"].append((filepath, lang, code))
    
    return organized


def generate_summary(
    created_files: List[Path],
    project_repo: Path
) -> str:
    """Gera resumo dos arquivos criados."""
    if not created_files:
        return "❌ Nenhum arquivo foi criado."
    
    relative_files = [str(f.relative_to(project_repo)) for f in created_files]
    
    summary = f"""
✅ {len(created_files)} arquivo(s) criado(s):

"""
    for f in relative_files:
        summary += f"   • {f}\n"
    
    return summary
