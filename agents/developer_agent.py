from crewai import Agent

developer_agent = Agent(
    role="Software Developer",
    goal="Escrever código funcional baseado nas tarefas",
    backstory="Engenheiro de software especialista em APIs e aplicações web",
    verbose=True
)