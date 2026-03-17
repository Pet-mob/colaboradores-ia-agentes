from crewai import Task
from agents.planner_agent import planner_agent
from agents.developer_agent import developer_agent
from agents.qa_agent import qa_agent

task_plan = Task(
    description="Criar um plano de desenvolvimento para um sistema de login com autenticação",
    agent=planner_agent
)

task_dev = Task(
    description="Escrever código de uma API simples de login",
    agent=developer_agent
)

task_qa = Task(
    description="Revisar o código da API de login e apontar possíveis problemas",
    agent=qa_agent
)