from fastapi import HTTPException, status, Depends
from fastapi.security import APIKeyHeader
from ..core import Settings

api_settings = Settings() # type: ignore
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_api_key(api_key: str = Depends(api_key_header)) -> str:
    if (api_key != api_settings.api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida ou não fornecida",
        )
    return api_key