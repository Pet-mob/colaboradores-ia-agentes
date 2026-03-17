from crewai import Agent

planner_agent = Agent(
    role="Product Planner",
    goal="Transformar ideias em tarefas técnicas",
    backstory="Especialista em planejamento de software e criação de backlog",
    verbose=True
)