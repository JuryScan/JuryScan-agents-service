from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core import api_config

from .routes import base_router, analyze_router

app = FastAPI(
    title=api_config.API_TITLE,
    description=api_config.API_DESCRIPTION,
    version=api_config.API_VERSION
)

# CORS config (via middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=api_config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adicionar routers
base_prefix = "/api/v1"
app.include_router(base_router, prefix=base_prefix)
app.include_router(analyze_router, prefix=base_prefix)