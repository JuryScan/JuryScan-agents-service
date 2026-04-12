from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Bem-vindo ao serviço de Orquestração de Agentes do JuryScan! Docs em /docs"}