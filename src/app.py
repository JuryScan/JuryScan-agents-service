from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .core import Settings, get_custom_openapi

from .routes import base_router, analyze_router
from .middlewares import verify_api_key_middleware

api_settings = Settings() # type: ignore
app = FastAPI(
    title=api_settings.api_title,
    description=api_settings.api_description,
    version=api_settings.api_version
)

# Configurar OpenAPI personalizado
app.openapi = get_custom_openapi(app, api_settings)

# CORS config (via middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=api_settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adicionar routers
app.include_router(base_router, dependencies=[Depends(verify_api_key_middleware)])
app.include_router(analyze_router, dependencies=[Depends(verify_api_key_middleware)])