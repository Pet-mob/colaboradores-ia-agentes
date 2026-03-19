from crewai import Crew
from pathlib import Path
from agents.planner_agent import planner_agent
from agents.developer_agent import developer_agent
from agents.qa_agent import qa_agent
from tasks.dev_tasks import create_tasks
from tasks.queue_manager import update_section
from tools.git_manager import create_demand_branch


def run_ai_team(filepath: Path) -> str:
    branch = create_demand_branch(filepath)
    print(f"📌 Trabalhando na branch: {branch}\n")

    tasks = create_tasks(filepath)

    crew = Crew(
        agents=[planner_agent, developer_agent, qa_agent],
        tasks=tasks,
        verbose=True
    )

    crew.kickoff()

    # Escreve o resultado de cada agente na sua seção do .md
    if tasks[0].output:
        update_section(filepath, "plan", tasks[0].output.raw)
    if tasks[1].output:
        update_section(filepath, "dev", tasks[1].output.raw)
    if tasks[2].output:
        update_section(filepath, "qa", tasks[2].output.raw)

    return tasks[2].output.raw if tasks[2].output else "Sem resultado"
