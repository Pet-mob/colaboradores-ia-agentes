import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Modelo padrão — troque por claude-sonnet-4-5-20250514 para tarefas mais complexas
DEFAULT_MODEL = "claude-haiku-3-5-20241022"