import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Modelo atual: Groq (free)
# Para migrar para Claude, troque por:
#   "claude-haiku-3-5-20241022"   → rápido e barato
#   "claude-sonnet-4-5-20250514"  → mais poderoso
DEFAULT_LLM = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)