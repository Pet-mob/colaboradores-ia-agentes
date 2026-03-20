import json
import os
import re
import subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECTS_DIR = Path(__file__).parent.parent / "projects"

# Mapeamento: nome do projeto (lowercase) → arquivo json
_PROJECT_FILES = {
    "pet.on.api": "pet_on_api.json",
    "petshop.webapp": "petshop_webapp.json",
    "pet.on.app": "pet_on_app.json",
    "petshop.app": "petshop_webapp.json",  # fallback
}


def _get_project_repo(project_name: str) -> Path | None:
    """Retorna o Path local do repositório do projeto, ou None se não encontrado."""
    key = project_name.lower().strip()
    filename = _PROJECT_FILES.get(key)
    if not filename:
        # Tenta match parcial
        for k, v in _PROJECT_FILES.items():
            if k in key or key in k:
                filename = v
                break

    if not filename:
        return None

    data = json.loads((PROJECTS_DIR / filename).read_text(encoding="utf-8"))
    local_path = data.get("local_path")
    return Path(local_path) if local_path else None


def _extract_project(demand_filepath: Path) -> str:
    """Lê o campo Projeto do arquivo de demanda."""
    try:
        text = demand_filepath.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "**Projeto:**" in line:
                return line.replace("**Projeto:**", "").strip()
    except Exception:
        pass
    return ""


def get_branch_name(demand_filepath: Path) -> str:
    stem = demand_filepath.stem  # ex: '044-bug-dados-incorretos'
    return f"demand/{stem}"


def create_demand_branch(demand_filepath: Path) -> str:
    """
    Cria e faz checkout de uma branch git no repositório do projeto da demanda.
    Se a branch já existir, apenas faz checkout.
    Retorna o nome da branch.
    """
    branch = get_branch_name(demand_filepath)
    project_name = _extract_project(demand_filepath)
    repo_path = _get_project_repo(project_name)

    if not repo_path or not repo_path.exists():
        print(f"[WARNING] Repositório local não encontrado para '{project_name}'. Branch não criada.")
        return branch

    try:
        result = subprocess.run(
            ["git", "branch", "--list", branch],
            cwd=str(repo_path),
            capture_output=True,
            text=True
        )

        if branch in result.stdout:
            subprocess.run(
                ["git", "checkout", branch],
                cwd=str(repo_path),
                check=True,
                capture_output=True,
                text=True
            )
            print(f"[CHECKOUT] Branch existente, checkout em '{repo_path.name}': {branch}")
        else:
            subprocess.run(
                ["git", "checkout", "-b", branch],
                cwd=str(repo_path),
                check=True,
                capture_output=True,
                text=True
            )
            print(f"[NEW BRANCH] Branch criada em '{repo_path.name}': {branch}")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Erro ao criar branch em '{repo_path}': {e.stderr.strip()}")

    return branch


def commit_and_push(demand_filepath: Path, branch: str) -> None:
    """
    Faz git add, commit e push da branch no repositório do projeto da demanda.
    """
    project_name = _extract_project(demand_filepath)
    repo_path = _get_project_repo(project_name)

    if not repo_path or not repo_path.exists():
        print(f"[WARNING] Repositório local não encontrado para '{project_name}'. Commit/push ignorado.")
        return

    demand_id = demand_filepath.stem  # ex: 044-bug-dados-incorretos
    commit_msg = f"feat({demand_id}): implementação gerada pelos agentes IA"

    try:
        # Garante que estamos na branch correta
        subprocess.run(
            ["git", "checkout", branch],
            cwd=str(repo_path), check=True, capture_output=True, text=True
        )

        # Verifica se há algo a commitar
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(repo_path), capture_output=True, text=True
        )

        if not status.stdout.strip():
            print(f"[INFO] Nenhuma alteração para commitar em '{repo_path.name}'.")
            return

        subprocess.run(
            ["git", "add", "."],
            cwd=str(repo_path), check=True, capture_output=True, text=True
        )
        print(f"[GIT] git add . em '{repo_path.name}'")

        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=str(repo_path), check=True, capture_output=True, text=True
        )
        print(f"[OK] Commit: {commit_msg}")

        # Monta URL autenticada com token se disponível
        token = os.getenv("GITHUB_TOKEN", "").strip()
        original_remote_url = None
        
        if token:
            # Salva URL original
            original_remote_url = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=str(repo_path), capture_output=True, text=True
            ).stdout.strip()
            
            # Injeta token na URL
            auth_url = re.sub(r"https://", f"https://{token}@", original_remote_url)
            
            # Atualiza remote temporariamente
            subprocess.run(
                ["git", "remote", "set-url", "origin", auth_url],
                cwd=str(repo_path), check=True, capture_output=True, text=True
            )
            
            try:
                subprocess.run(
                    ["git", "push", "-u", "origin", branch],
                    cwd=str(repo_path), check=True, capture_output=True, text=True
                )
            finally:
                # Restaura URL original (sem token exposto)
                subprocess.run(
                    ["git", "remote", "set-url", "origin", original_remote_url],
                    cwd=str(repo_path), check=True, capture_output=True, text=True
                )
        else:
            # Sem token, usa configuração default de credenciais
            subprocess.run(
                ["git", "push", "-u", "origin", branch],
                cwd=str(repo_path), check=True, capture_output=True, text=True
            )
        
        print(f"[PUSH] Push para origin/{branch} em '{repo_path.name}'")
        
        # Atualiza referências remotas localmente
        try:
            subprocess.run(
                ["git", "fetch", "--prune"],
                cwd=str(repo_path), check=True, capture_output=True, text=True, timeout=30
            )
        except subprocess.CalledProcessError:
            pass  # Não é crítico se falhar

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Erro no commit/push em '{repo_path}': {e.stderr.strip()}")
