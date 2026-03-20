#!/usr/bin/env python3
"""
Test: Validar criação e push de branches para GitHub
"""

import subprocess
from pathlib import Path
from tools.git_manager import (
    create_demand_branch, 
    commit_and_push, 
    get_branch_name,
    _get_project_repo,
    _extract_project
)

def test_branch_creation_and_push():
    """Testa se branches estão sendo criadas e pushadas corretamente"""
    
    print("\n" + "=" * 80)
    print("TESTE: Validação de Branches no GitHub")
    print("=" * 80)
    
    # Pega uma demanda que foi processada
    demand_file = Path("demands/done/013-sistema-confirmacao-servicos.md")
    
    if not demand_file.exists():
        print(f"❌ Arquivo de demanda não encontrado: {demand_file}")
        return False
    
    # Extrai informações
    branch = get_branch_name(demand_file)
    project_name = _extract_project(demand_file)
    repo_path = _get_project_repo(project_name)
    
    print(f"\n📋 Informações da Demanda:")
    print(f"   Arquivo: {demand_file.name}")
    print(f"   Projeto: {project_name}")
    print(f"   Branch: {branch}")
    print(f"   Repo Local: {repo_path}")
    
    if not repo_path or not repo_path.exists():
        print(f"\n❌ Repositório não encontrado: {repo_path}")
        return False
    
    # Testa se branch local existe
    print(f"\n🔍 Verificando branch local...")
    try:
        result = subprocess.run(
            ["git", "branch", "-a"],
            cwd=str(repo_path),
            capture_output=True,
            text=True,
            timeout=10
        )
        
        all_branches = result.stdout
        has_local = branch in all_branches
        has_remote = f"remotes/origin/{branch}" in all_branches
        
        print(f"   Local: {'✅' if has_local else '❌'} {branch}")
        print(f"   Remote: {'✅' if has_remote else '❌'} remotes/origin/{branch}")
        
        if not has_local:
            print(f"\n   ⚠️ Branch local '{branch}' NÃO encontrada!")
            print(f"   Branches locais disponíveis:")
            for b in all_branches.split('\n'):
                if b.strip() and not b.startswith('remotes'):
                    print(f"      - {b.strip()}")
        
        if not has_remote:
            print(f"\n   ⚠️ Branch remota 'origin/{branch}' NÃO encontrada no GitHub!")
            print(f"   Branches remotas disponíveis:")
            for b in all_branches.split('\n'):
                if b.startswith('remotes/origin/demand'):
                    print(f"      - {b.replace('remotes/origin/', '')}")
        
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erro ao listar branches: {e.stderr}")
        return False
    
    # Testa git log da branch
    print(f"\n📝 Verif icando commits na branch...")
    try:
        result = subprocess.run(
            ["git", "log", branch, "--oneline", "-5"],
            cwd=str(repo_path),
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0 and result.stdout.strip():
            print(f"   ✅ Commits encontrados:")
            for line in result.stdout.strip().split('\n')[:3]:
                print(f"      - {line}")
        else:
            print(f"   ❌ Nenhum commit encontrado na branch")
            
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erro ao checar commits: {e.stderr}")
    
    # Testa conexão com GitHub
    print(f"\n🌐 Verificando conexão com GitHub...")
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--heads", "origin"],
            cwd=str(repo_path),
            capture_output=True,
            text=True,
            timeout=15
        )
        
        if result.returncode == 0:
            print(f"   ✅ Conexão com GitHub OK")
            
            # Procura branches da demanda
            remote_branches = result.stdout
            matching = [b for b in remote_branches.split('\n') if branch in b]
            
            if matching:
                print(f"   ✅ Branch found no remote:")
                for b in matching:
                    print(f"      - {b}")
            else:
                print(f"   ❌ Branch '{branch}' NÃO encontrada no remote")
                print(f"   Branches demand/ no remote:")
                demand_branches = [b for b in remote_branches.split('\n') if 'demand/' in b]
                for b in demand_branches[:5]:
                    if b.strip():
                        print(f"      - {b.split()[-1]}")
        else:
            print(f"   ❌ Erro ao conectar com GitHub: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print(f"   ⚠️ Timeout ao conexão com GitHub (sem internet?)")
    except Exception as e:
        print(f"   ❌ Erro: {e}")
    
    print("\n" + "=" * 80)
    return has_local and has_remote


if __name__ == "__main__":
    success = test_branch_creation_and_push()
    
    if success:
        print("\n✅ TESTE PASSOU - Branches estão sendo criadas e pushadas corretamente!\n")
    else:
        print("\n❌ TESTE FALHOU - Há problemas com criação/push de branches\n")
        print("AÇÕES PARA RESOLVER:")
        print("1. Verificar se o token GITHUB_TOKEN está válido")
        print("2. Verificar se os repositórios locais estão configurados com origin")
        print("3. Rodar 'git remote -v' em cada repo para confirmar remote origin")
        print("4. Testar manualmente: git push -u origin demand/013-sistema-confirmacao-servicos")
