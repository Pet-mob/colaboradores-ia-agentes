from crewai import Task
from pathlib import Path
from agents.planner_agent import planner_agent
from agents.developer_agent import developer_agent
from agents.qa_agent import qa_agent
from tools.context_enricher_v2 import (
    enrich_planner_prompt,
    enrich_developer_prompt,
    enrich_qa_prompt,
)
from tools.stack_detector import (
    detect_stacks_from_demand,
    get_primary_stack,
    get_affected_stacks,
    get_stack_appropriate_context,
    get_validation_instructions,
)
from tools.clarification_system import (
    ClarificationGenerator,
    extract_entity_names_from_demand,
)


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

    # 🔍 NOVO: Detectar stacks afetados
    stacks_scores = detect_stacks_from_demand(content, project)
    primary_stack = get_primary_stack(stacks_scores)
    affected_stacks = get_affected_stacks(stacks_scores, threshold=0.5)
    stack_validation = get_validation_instructions(affected_stacks)

    # 🤔 NOVO: Gerar clarification questions antes do plano
    entity_names = extract_entity_names_from_demand(content)
    clar_gen = ClarificationGenerator()
    
    tasks = []
    clarification_task = None
    
    # Se há entidades mencionadas que existem, criar task de clarificação
    if clar_gen.should_ask_clarifications(entity_names):
        clarification_prompt = clar_gen.generate_clarification_prompt_for_planner(content, entity_names)
        
        clarification_full_prompt = (
            f"Você é o Arquiteto Técnico Senior da equipe Petmob.\n\n"
            f"ANTES de criar o plano técnico, responda às seguintes perguntas sobre a demanda: **{title}**\n\n"
            f"{clarification_prompt}\n\n"
            f"Escreva suas respostas em Markdown claro, pois elas guiarão o desenvolvimento."
        )
        
        clarification_task = Task(
            description=clarification_full_prompt,
            expected_output="Respostas claras às perguntas de clarificação, indicando: entidades a reutilizar/estender, propriedades a adicionar, e decisões de arquitetura",
            agent=planner_agent
        )
        tasks.append(clarification_task)

    # Enriquece prompts com contexto V2
    planner_base_prompt = (
        f"Você é o Arquiteto Técnico Senior da equipe Petmob.\n\n"
        f"Crie um plano técnico detalhado para a demanda: **{title}**\n\n"
        f"Tipo: {demand_type}\n"
        f"Projeto Afetado: {project}\n\n"
        f"Descrição:\n{description}\n\n"
    )
    
    # Se houve clarification, incluir as respostas no prompt do plano
    if clarification_task:
        planner_base_prompt += (
            f"Use as clarifications respondidas acima para guiar este plano.\n"
            f"Priorize REUTILIZAR entidades e repositories existentes ao invés de criar novos.\n\n"
        )
    
    planner_base_prompt += (
        f"Seu plano deve decompor a demanda em tarefas pequenas e testáveis, "
        f"identificar entidades afetadas, endpoints necessários, telas que mudam, e riscos."
    )
    
    planner_prompt, planner_stats = enrich_planner_prompt(planner_base_prompt, title)
    
    task_plan = Task(
        description=planner_prompt,
        expected_output="Plano técnico completo em Markdown com tarefas, critérios de aceite, tecnologias e estimativa de complexidade",
        agent=planner_agent,
        context=[clarification_task] if clarification_task else []
    )
    
    tasks.append(task_plan)

    # 🔧 NOVO: Developer prompt com contexto de stack específico
    developer_base_prompt = (
        f"Você é o Senior Software Engineer da equipe Petmob.\n\n"
        f"Implemente a solução para a demanda: **{title}**\n\n"
        f"Contexto do Projeto: {project}\n\n"
        f"Use o plano técnico fornecido pelo Planner Agent como referência.\n\n"
        f"⭐ IMPORTANTE: Reutilize entidades e repositories EXISTENTES. Crie novos apenas se não existirem.\n\n"
        f"{stack_validation}\n\n"
        f"{get_stack_appropriate_context(primary_stack)}"
    )
    
    developer_prompt, developer_stats = enrich_developer_prompt(
        developer_base_prompt, title, project.lower()
    )

    task_dev = Task(
        description=developer_prompt,
        expected_output="Implementação completa com código pronto para produção formatado com '# File:' headers, explicações e guias de integração",
        agent=developer_agent,
        context=[task_plan]
    )
    
    tasks.append(task_dev)

    # QA prompt com contexto de testes
    qa_base_prompt = (
        f"Você é o Quality Assurance Architect da equipe Petmob.\n\n"
        f"Analise a implementação de: **{title}**\n\n"
        f"Projeto: {project}\n\n"
        f"Valide conformidade técnica, segurança, performance, casos edge, e testes."
    )
    
    qa_prompt, qa_stats = enrich_qa_prompt(qa_base_prompt, title)

    task_qa = Task(
        description=qa_prompt,
        expected_output="Análise detalhada de qualidade com problemas, sugestões e veredicto final (✅ / ⚠️ / ❌)",
        agent=qa_agent,
        context=[task_plan, task_dev]
    )
    
    tasks.append(task_qa)

    return tasks

