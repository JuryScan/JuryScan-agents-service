from pydantic import BaseModel
from typing import Optional, Any


class AnalyzeResponse(BaseModel):
    """Resposta da análise de documento CNIS"""
    status: str
    message: str
    result: Optional[Any] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Análise concluída com sucesso",
                "result": {
                    "status_geral": "completo",
                    "sumario_juridico": {},
                    "sumario_comum": {}
                }
            }
        }