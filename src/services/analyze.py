"""Serviço de análise de documentos CNIS usando uma crew de agentes"""
import io
import logging
from typing import Any, Dict

import pdfplumber

from ..crew import JuryScanAgentsCrew
from ..schemas.analyze import AnalysisResult

logger = logging.getLogger(__name__)


class AnalyzeService:
    """Service para gerenciar análise de documentos CNIS com a crew de agentes"""

    def __init__(self):
        self.crew = JuryScanAgentsCrew()

    @staticmethod
    def _extract_text(pdf_content: bytes) -> str:
        with pdfplumber.open(io.BytesIO(pdf_content)) as pdf:
            texto = "\n".join((page.extract_text() or "") for page in pdf.pages)
        if not texto.strip():
            raise ValueError("Não foi possível extrair texto do PDF")
        return texto

    def analyze_cnis(self, pdf_content: bytes) -> Dict[str, Any]:
        try:
            logger.info("Iniciando análise do documento CNIS")

            texto_cnis = self._extract_text(pdf_content)
            logger.info("Texto extraído do CNIS (%d caracteres). Disparando a crew...", len(texto_cnis))

            result = self.crew.crew().kickoff(inputs={'conteudo_cnis': texto_cnis})

            analysis_result = getattr(result, 'pydantic', None)
            if not isinstance(analysis_result, AnalysisResult):
                raw = getattr(result, 'raw', result)
                logger.error("Crew não retornou AnalysisResult validado. Raw: %s", str(raw)[:1000])
                raise ValueError("Crew não devolveu AnalysisResult validado pelo schema")

            logger.info("Análise concluída com sucesso")
            return {
                "status": "success",
                "message": "Análise do CNIS realizada com sucesso",
                "result": analysis_result,
            }

        except Exception as e:
            logger.error("Erro ao analisar CNIS: %s", e, exc_info=True)
            return {
                "status": "error",
                "message": f"Erro ao processar o documento: {str(e)}",
                "result": None,
            }
