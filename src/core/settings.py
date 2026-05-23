from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = Path(__file__).parent.parent / ".env"

class Settings(BaseSettings):
    """Configurações globais do serviço"""
    # API
    api_title: str = "Serviço de Agentes do JuryScan"
    api_description: str = "1.0.0"
    api_version: str = "Serviço de orquestração de agentes de IA para o sistema JuryScan"
    api_key: str
    # CORS
    cors_origins: list = [
        "http://localhost:8000", 
        "http://localhost:8080",
        "http://localhost:8081"
    ]
    # GEMINI
    google_api_key: str
    llm_model: str

    model_config = SettingsConfigDict( # type: ignore
        env_file=env_path,
        env_file_encoding='utf-8'
    )