from fastapi.openapi.utils import get_openapi
from typing import Any, Callable, Dict

def get_custom_openapi(app: Any, api_settings: Any) -> Callable:
    """
    Retorna função personalizada para gerar o esquema OpenAPI
    """
    def custom_openapi() -> Dict[str, Any]:
        if app.openapi_schema:
            return app.openapi_schema
        # Gerar esquema OpenAPI personalizado com informações do Settings
        openapi_schema = get_openapi(
            title=api_settings.api_title,
            version=api_settings.api_version,
            description=api_settings.api_description,
            routes=app.routes
        )
        # security schema para API Key
        openapi_schema["components"]["securitySchemes"] = {
            "api_key": {
                "type": "apiKey",
                "in": "header",
                "name": "X-API-Key"
            }
        }

        # Adicionar segurança em todas as rotas
        for path in openapi_schema.get("paths", {}).values():
            for operation in path.values():
                operation["security"] = [{"api_key": []}]

        openapi_schema["security"] = [{"api_key": []}]
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return custom_openapi