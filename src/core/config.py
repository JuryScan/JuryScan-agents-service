import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class APIConfig:
    """Configurações globais do serviço"""
    # API
    API_TITLE: str = "Serviço de Agentes do JuryScan"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "Serviço de orquestração de agentes de IA para o sistema JuryScan"
    # CORS
    CORS_ORIGINS: list = ["*"]
    # GEMINI
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gemini-2.5-flash")

api_config = APIConfig()