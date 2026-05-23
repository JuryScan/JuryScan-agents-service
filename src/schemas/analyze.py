from pydantic import BaseModel, Field
from typing import Optional, List


class DadosExtraidos(BaseModel):
    """Dados básicos extraídos do documento CNIS"""
    nome: Optional[str] = Field(None, description="Nome do segurado")
    cpf: Optional[str] = Field(None, description="CPF do segurado")
    nome_mae: Optional[str] = Field(None, description="Nome da mãe do segurado")
    total_vinculos: Optional[int] = Field(None, description="Número total de vínculos empregatícios")
    periodo_inicial: Optional[str] = Field(None, description="Data do vínculo mais antigo")
    periodo_final: Optional[str] = Field(None, description="Data do vínculo mais recente")


class Failure(BaseModel):
    """Falha ou inconsistência encontrada com detalhes estruturados"""
    titulo: str = Field(..., description="Título da falha encontrada")
    severidade: str = Field(..., description="Nível de severidade", pattern="^(ALTA|MEDIA|BAIXA|INFO)$")
    descricao: str = Field(..., description="Descrição detalhada do problema")
    sugestaoCorrecao: str = Field(..., description="Sugestão de correção para a falha")
    confianca: float = Field(..., ge=0.0, le=1.0, description="Nível de confiança entre 0 e 1")


class AnalysisResult(BaseModel):
    """Resultado final da análise estruturado conforme especificação"""
    titulo: str = Field(..., description="Título geral da análise")
    descricaoGeral: str = Field(..., description="Descrição geral dos achados")
    dados_extraidos: Optional[DadosExtraidos] = Field(None, description="Dados básicos extraídos do CNIS")
    failures: List[Failure] = Field(default_factory=list, description="Lista de falhas encontradas")
    relatorio_sumario_juridico: Optional[str] = Field(None, description="Análise técnica em linguagem jurídica")
    sumario: Optional[str] = Field(None, description="Resumo em linguagem acessível para o cidadão")


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
                    "titulo": "Análise do CNIS - Inconsistências Detectadas",
                    "descricaoGeral": "Foi identificada 1 inconsistência no histórico previdenciário do segurado",
                    "dados_extraidos": {
                        "nome": "João da Silva Santos",
                        "cpf": "123.456.789-01",
                        "nome_mae": "Maria de Fátima",
                        "total_vinculos": 5,
                        "periodo_inicial": "2010-01-15",
                        "periodo_final": "2023-12-31"
                    },
                    "failures": [
                        {
                            "titulo": "Período sem data de demissão",
                            "severidade": "ALTA",
                            "descricao": "Encontrado vínculo empregatício em 2015 sem data de término registrada",
                            "sugestaoCorrecao": "Solicitar ao empregador confirmação do período final de vínculo",
                            "confianca": 0.95
                        }
                    ],
                    "relatorio_sumario_juridico": "Conforme análise técnica previdenciária, o segurado apresenta lacunas em seu histórico contributivo...",
                    "sumario": "Detectamos um período de trabalho sem registro de término. Recomendamos entrar em contato com o empregador para regularizar."
                }
            }
        }