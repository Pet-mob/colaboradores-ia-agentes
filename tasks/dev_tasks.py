from crewai import Task
from pathlib import Path
from agents.planner_agent import planner_agent
from agents.developer_agent import developer_agent
from agents.qa_agent import qa_agent


def _extract_metadata(text: str, field: str) -> str:
    for line in text.split("\n"):
        if f"**{field}:**" in line:
            return line.replace(f"**{field}:**", "").strip()
    return ""


def _extract_description(text: str) -> str:
    start = text.find("## Descrição")
    end = text.find("---", start)
    if start == -1:
        return ""
    return text[start + len("## Descrição"):end].strip()


def create_tasks(filepath: Path) -> list:
    content = filepath.read_text(encoding="utf-8")
    title = content.split("\n")[0].replace("# Demanda:", "").strip()
    project = _extract_metadata(content, "Projeto")
    demand_type = _extract_metadata(content, "Tipo")
    description = _extract_description(content)

    title = demand["title"]
    description = demand["description"]
    project = demand.get("project", "geral")
    demand_type = demand.get("type", "feature")

    task_plan = Task(
        description=(
            f"Você é o Planner Agent da equipe Petmob.\n\n"
            f"Crie um plano técnico detalhado para a demanda abaixo:\n\n"
            f"**Projeto:** {project}\n"
            f"**Tipo:** {demand_type}\n"
            f"**Título:** {title}\n"
            f"**Descrição:** {description}\n\n"
            f"Produza um plano estruturado em Markdown com:\n"
            f"- Lista numerada de tarefas técnicas\n"
            f"- Critérios de aceite para cada tarefa\n"
            f"- Stack e tecnologias envolvidas\n"
            f"- Estimativa de complexidade (baixa/média/alta)"
        ),
        expected_output="Plano técnico completo em Markdown",
        agent=planner_agent
    )

    task_dev = Task(
        description=(
            f"Você é o Developer Agent da equipe Petmob.\n\n"
            f"Implemente a solução para a demanda abaixo, seguindo o plano do Planner Agent:\n\n"
            f"**Projeto:** {project}\n"
            f"**Tipo:** {demand_type}\n"
            f"**Título:** {title}\n"
            f"**Descrição:** {description}\n\n"
            f"Escreva o código completo com:\n"
            f"- Blocos de código com a linguagem correta\n"
            f"- Comentários nas partes importantes\n"
            f"- Explicação das decisões de arquitetura\n"
            f"- Instruções de uso/integração"
        ),
        expected_output="Código implementado em Markdown com blocos de código e explicações",
        agent=developer_agent,
        context=[task_plan]
    )

    task_qa = Task(
        description=(
            f"Você é o QA Agent da equipe Petmob.\n\n"
            f"Revise a implementação da demanda abaixo produzida pelo Developer Agent:\n\n"
            f"**Projeto:** {project}\n"
            f"**Título:** {title}\n\n"
            f"Produza um relatório de qualidade com:\n"
            f"- Bugs ou problemas encontrados\n"
            f"- Vulnerabilidades de segurança (se houver)\n"
            f"- Sugestões de melhoria\n"
            f"- Veredicto final: ✅ Aprovado / ⚠️ Aprovado com ressalvas / ❌ Reprovado"
        ),
        expected_output="Relatório de qualidade completo em Markdown com veredicto final",
        agent=qa_agent,
        context=[task_plan, task_dev]
    )

    return [task_plan, task_dev, task_qa]

