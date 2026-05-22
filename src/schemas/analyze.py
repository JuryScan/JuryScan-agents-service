from pydantic import BaseModel, Field
from typing import Optional, List


class Validacoes(BaseModel):
    """Resultado das validações realizadas"""
    cpf_regular: Optional[bool] = None
    dados_identidade_validos: Optional[bool] = None
    mensagens_validacao: List[str] = Field(default_factory=list)


class Inconsistencia(BaseModel):
    """Inconsistência encontrada com grau de confiança"""
    descricao: str
    confianca: float = Field(..., ge=0.0, le=1.0)  # Valor entre 0 e 1


class Relatorio(BaseModel):
    """Relatório final com análises jurídica e comum"""
    sumario_juridico: Optional[str] = None
    sumario_comum: Optional[str] = None


class AnalysisResult(BaseModel):
    """Resultado final mapeado do JSON da crew"""
    validacoes: Optional[Validacoes] = None
    inconsistencias: List[Inconsistencia] = Field(default_factory=list)
    relatorio: Optional[Relatorio] = None


class AnalyzeResponse(BaseModel):
    """Resposta da análise de documento CNIS"""
    status: str
    message: str
    result: Optional[AnalysisResult] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Análise do CNIS realizada com sucesso",
                "result": {
                    "validacoes": {
                        "cpf_regular": True,
                        "dados_identidade_validos": True,
                        "mensagens_validacao": []
                    },
                    "inconsistencias": [
                        {"descricao": "Período sem data de demissão em 2015", "confianca": 0.95}
                    ],
                    "relatorio": {
                        "sumario_juridico": "Análise técnica jurídica do documento...",
                        "sumario_comum": "Resumo claro para o usuário final..."
                    }
                }
            }
        }