"""Serviço de análise de documentos CNIS usando uma crew de agentes"""
from typing import Dict, Any
import logging
import base64
import json
from ..crew import JuryScanAgentsCrew
from ..schemas.analyze import AnalysisResult

logger = logging.getLogger(__name__)

class AnalyzeService:
    """Service para gerenciar análise de documentos CNIS com a crew de agentes"""

    def __init__(self):
        """Inicializa o serviço com a crew"""
        self.crew = JuryScanAgentsCrew()

    def _parse_crew_json_result(self, raw_result: Any) -> AnalysisResult:
        """
        Converte o resultado bruto da crew em um AnalysisResult validado.
        """
        try:
            # Extrair .output se for objeto da crew
            if hasattr(raw_result, 'output'):
                result_str = raw_result.output
            else:
                result_str = raw_result if isinstance(raw_result, str) else str(raw_result)
            
            # Parsear JSON
            logger.info("Parseando resultado em JSON...")
            result_dict = json.loads(result_str.strip())
            
            logger.info(f"JSON parseado com sucesso: {json.dumps(result_dict, ensure_ascii=False, indent=2)[:500]}")
            
            # Validar contra schema Pydantic
            analysis_result = AnalysisResult(**result_dict)
            logger.info("Resultado validado com sucesso contra schema AnalysisResult")
            
            return analysis_result
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao fazer parse do JSON: {str(e)}")
            logger.error(f"Raw result que falhou: {raw_result}")
            raise ValueError(f"Crew retornou conteúdo inválido que não é JSON: {str(e)}") from e
        except Exception as e:
            logger.error(f"Erro ao validar contra schema AnalysisResult: {str(e)}")
            logger.error(f"Raw result que falhou: {raw_result}")
            raise ValueError(f"Erro ao mapear resultado da crew para schema: {str(e)}") from e

    def analyze_cnis(self, pdf_content: bytes) -> Dict[str, Any]:
        """
        Analisa um documento CNIS usando a crew de agentes.
        """
        try:
            logger.info("Iniciando análise do documento CNIS")
            
            # Converte conteúdo PDF para base64
            pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')  
            inputs = {
                'conteudo_cnis': pdf_base64
            }
            
            # Executa a crew de forma sequencial
            result = self.crew.crew().kickoff(inputs=inputs)
            
            # Parsear e validar JSON
            analysis_result = self._parse_crew_json_result(result)
            
            return {
                "status": "success",
                "message": "Análise do CNIS realizada com sucesso",
                "result": analysis_result
            }
        
        except Exception as e:
            logger.error(f"Erro ao analisar CNIS: {str(e)}", exc_info=True)
            return {
                "status": "error",
                "message": f"Erro ao processar o documento: {str(e)}",
                "result": None
            }