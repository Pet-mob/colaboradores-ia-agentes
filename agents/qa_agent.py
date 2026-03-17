from crewai import Agent

qa_agent = Agent(
    role="QA Engineer",
    goal="Revisar código e identificar possíveis erros",
    backstory="Especialista em testes e qualidade de software",
    verbose=True
)