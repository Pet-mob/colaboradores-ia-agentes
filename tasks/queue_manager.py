import shutil
from datetime import datetime
from pathlib import Path

DEMANDS_DIR = Path(__file__).parent.parent / "demands"
PENDING_DIR = DEMANDS_DIR / "pending"
IN_PROGRESS_DIR = DEMANDS_DIR / "in_progress"
DONE_DIR = DEMANDS_DIR / "done"

PROJECTS = ["pet.on.Api", "petshop.webapp", "pet.on.app", "geral"]
DEMAND_TYPES = ["feature", "bugfix", "refactor", "analysis"]


def _ensure_dirs() -> None:
    for d in [PENDING_DIR, IN_PROGRESS_DIR, DONE_DIR]:
        d.mkdir(parents=True, exist_ok=True)


def add_demand(title: str, description: str, project: str = "geral", demand_type: str = "feature") -> Path:
    _ensure_dirs()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = title.lower().replace(" ", "-")[:40]
    filepath = PENDING_DIR / f"{timestamp}_{slug}.md"
    content = f"""# Demanda: {title}

**Projeto:** {project}
**Tipo:** {demand_type}
**Criada em:** {datetime.now().strftime("%d/%m/%Y %H:%M")}

## Descrição

{description}

---

## 📋 Planejamento

*Aguardando processamento pelo Planner Agent...*

---

## 💻 Implementação

*Aguardando processamento pelo Developer Agent...*

---

## ✅ Revisão de Qualidade

*Aguardando processamento pelo QA Agent...*
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


def list_demands(status: str = None) -> list:
    _ensure_dirs()
    dirs = {"pending": PENDING_DIR, "in_progress": IN_PROGRESS_DIR, "done": DONE_DIR}
    result = []
    for s, d in dirs.items():
        if status and s != status:
            continue
        for f in sorted(d.glob("*.md")):
            result.append({"status": s, "file": f, "name": f.name})
    return result


def get_next_pending() -> Path | None:
    _ensure_dirs()
    files = sorted(PENDING_DIR.glob("*.md"))
    return files[0] if files else None


def move_to_in_progress(filepath: Path) -> Path:
    dest = IN_PROGRESS_DIR / filepath.name
    shutil.move(str(filepath), str(dest))
    return dest


def move_to_done(filepath: Path) -> Path:
    dest = DONE_DIR / filepath.name
    shutil.move(str(filepath), str(dest))
    return dest


def update_section(filepath: Path, section: str, content: str) -> None:
    placeholders = {
        "plan": "*Aguardando processamento pelo Planner Agent...*",
        "dev": "*Aguardando processamento pelo Developer Agent...*",
        "qa": "*Aguardando processamento pelo QA Agent...*",
    }
    text = filepath.read_text(encoding="utf-8")
    updated = text.replace(placeholders[section], content.strip())
    filepath.write_text(updated, encoding="utf-8")



        f.write(f"\n{'='*60}\n")
        f.write(f"RESULTADO:\n\n{result}\n")
