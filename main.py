from config.settings import OPENAI_API_KEY
from agents.orchestrator import run_ai_team

if __name__ == "__main__":
    
    print("Iniciando equipe de agentes IA...\n")

    resultado = run_ai_team()

    print("\nResultado final:\n")
    print(resultado)