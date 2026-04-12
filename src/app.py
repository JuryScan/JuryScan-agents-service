from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core import Settings

from .routes import base_router, analyze_router

api_settings = Settings() # type: ignore
app = FastAPI(
    title=api_settings.api_title,
    description=api_settings.api_description,
    version=api_settings.api_version
)

# CORS config (via middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=api_settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adicionar routers
app.include_router(base_router)
app.include_router(analyze_router)