from crewai import Agent
from config.settings import DEFAULT_LLM

developer_agent = Agent(
    role="Software Developer",
    goal="Escrever código limpo, funcional e bem estruturado baseado nas tarefas recebidas",
    backstory=(
        "Engenheiro de software full-stack especializado em .NET/C# para APIs, "
        "Vue.js/JavaScript para aplicações web e React Native para apps mobile. "
        "Segue boas práticas de arquitetura, escreve código modular e documentado."
    ),
    llm=DEFAULT_LLM,
    verbose=True
)