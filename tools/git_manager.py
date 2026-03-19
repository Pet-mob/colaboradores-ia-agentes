import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def get_branch_name(demand_filepath: Path) -> str:
    """Deriva o nome da branch a partir do nome do arquivo de demanda."""
    stem = demand_filepath.stem  # ex: '044-bug-dados-incorretos'
    return f"demand/{stem}"


def create_demand_branch(demand_filepath: Path) -> str:
    """
    Cria e faz checkout de uma branch git para a demanda informada.
    Se a branch já existir, apenas faz checkout.
    Retorna o nome da branch.
    """
    branch = get_branch_name(demand_filepath)

    try:
        # Verifica se a branch já existe localmente
        result = subprocess.run(
            ["git", "branch", "--list", branch],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True
        )

        if branch in result.stdout:
            subprocess.run(
                ["git", "checkout", branch],
                cwd=str(REPO_ROOT),
                check=True,
                capture_output=True,
                text=True
            )
            print(f"🔀 Branch existente, fazendo checkout: {branch}")
        else:
            subprocess.run(
                ["git", "checkout", "-b", branch],
                cwd=str(REPO_ROOT),
                check=True,
                capture_output=True,
                text=True
            )
            print(f"🌿 Branch criada: {branch}")

    except subprocess.CalledProcessError as e:
        print(f"⚠️  Erro ao criar/checar branch git: {e.stderr.strip()}")

    return branch
