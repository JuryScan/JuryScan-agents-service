"""Serviço de análise de documentos CNIS usando uma crew de agentes"""
from typing import Dict, Any
import logging
import base64
from ..crew import JuryScanAgentsCrew

logger = logging.getLogger(__name__)

class AnalyzeService:
    """Service para gerenciar análise de documentos CNIS com a crew de agentes"""

    def __init__(self):
        """Inicializa o serviço com a crew"""
        self.crew = JuryScanAgentsCrew()

    def analyze_cnis(self, pdf_content: bytes) -> Dict[str, Any]:
        """
        Analisa um documento CNIS usando a crew de agentes.
        O agente especialista usará a ferramenta de extração para processar o PDF.

        Ao final do processo, o agente gerador de relatório compilará um resumo jurídico e um sumário comum.
        """
        try:
            logger.info("Iniciando análise do documento CNIS")
            
            # Converte conteúdo PDF para base64
            pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')  
            inputs = {
                'conteudo_pdf_base64': pdf_base64
            }
            
            # Executa a crew de forma sequencial
            result = self.crew.crew().kickoff(inputs=inputs)
            
            logger.info("Análise concluída com sucesso")
            
            return {
                "status": "success",
                "message": "Análise do CNIS realizada com sucesso",
                "result": result
            }
        
        except Exception as e:
            logger.error(f"Erro ao analisar CNIS: {str(e)}", exc_info=True)
            return {
                "status": "error",
                "message": f"Erro ao processar o documento: {str(e)}",
                "result": None
            }