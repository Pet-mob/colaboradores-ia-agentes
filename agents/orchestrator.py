from crewai import Crew
from pathlib import Path
from agents.planner_agent import planner_agent
from agents.developer_agent import developer_agent
from agents.qa_agent import qa_agent
from tasks.dev_tasks import create_tasks
from tasks.queue_manager import update_section
from tools.git_manager import create_demand_branch, commit_and_push, _get_project_repo, _extract_project, get_branch_name
from tools.agents_validator import generate_validation_report, print_validation_report
from tools.retry_handler import retry_with_backoff, RetryConfig
from tools.code_generator import extract_code_blocks, create_project_files, generate_summary


def run_ai_team(filepath: Path) -> str:
    branch = create_demand_branch(filepath)
    print(f"[WORKING] Trabalhando na branch: {branch}\n")

    tasks = create_tasks(filepath)

    crew = Crew(
        agents=[planner_agent, developer_agent, qa_agent],
        tasks=tasks,
        verbose=True
    )

    # Executa crew com retry automático em caso de rate limit
    print("[STARTING] Iniciando execução dos agents...\n")
    retry_config = RetryConfig(
        max_retries=5,
        initial_delay=2,
        max_delay=300,
        backoff_factor=2.0,
        exponential=True
    )
    
    try:
        retry_with_backoff(
            crew.kickoff,
            config=retry_config,
            error_types=(Exception,)
        )
    except Exception as e:
        print(f"\n[ERROR] Execução falhou após múltiplas tentativas: {e}")
        raise

    # Escreve o resultado de cada agente na sua seção do .md
    if tasks[0].output:
        update_section(filepath, "plan", tasks[0].output.raw)
    if tasks[1].output:
        update_section(filepath, "dev", tasks[1].output.raw)
    if tasks[2].output:
        update_section(filepath, "qa", tasks[2].output.raw)

    # 🆕 Extrai e cria os arquivos de código gerados pela Developer Agent
    print("\n[CREATING] Criando arquivos de código no repositório...\n")
    project_name = _extract_project(filepath)
    repo_path = _get_project_repo(project_name)
    
    if repo_path and repo_path.exists() and tasks[1].output:
        dev_output = tasks[1].output.raw
        code_blocks = extract_code_blocks(dev_output)
        
        if code_blocks:
            created_files = create_project_files(repo_path, code_blocks, project_type="dotnet")
            summary = generate_summary(created_files, repo_path)
            print(summary)
        else:
            print("[INFO] Nenhum bloco de código foi extraído da output do Developer.\n")

    print("\n[COMMITTING] Commitando e fazendo push das alterações...")
    commit_and_push(filepath, branch)

    # Valida a execução dos agents
    print("\n[VALIDATING] Validando execução dos agents...\n")
    
    agent_outputs = {
        "Planner": tasks[0].output.raw if tasks[0].output else "",
        "Developer": tasks[1].output.raw if tasks[1].output else "",
        "QA": tasks[2].output.raw if tasks[2].output else ""
    }
    
    branch_name = get_branch_name(filepath)
    
    # Gera relatório de validação
    report = generate_validation_report(
        filepath.stem,  # nome da demanda
        agent_outputs,
        repo_path=repo_path,
        branch=branch_name
    )
    
    # Exibe o relatório
    print_validation_report(report)
    
    return tasks[2].output.raw if tasks[2].output else "Sem resultado"
