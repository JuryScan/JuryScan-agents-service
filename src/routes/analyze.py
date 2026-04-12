"""Rotas para análise de documentos CNIS"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from ..schemas.analyze import AnalyzeResponse
from ..services.analyze import AnalyzeService

router = APIRouter(
    prefix="/api/v1",
    tags=["analyze"]
)
analyze_service = AnalyzeService()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(file: UploadFile = File(...)) -> AnalyzeResponse:
    """
    Analisa um documento CNIS (PDF) usando a crew de agentes.
    O arquivo é enviado para a crew, que usa a ferramenta de extração do agente.
    """
    try:
        # Valida se é PDF
        if file.filename and not file.filename.lower().endswith('.pdf'):
            raise HTTPException(
                status_code=400,
                detail="Apenas arquivos PDF são suportados"
            )
        
        # Lê o conteúdo do arquivo PDF
        content = await file.read()
        if not content:
            raise HTTPException(
                status_code=400,
                detail="Arquivo vazio"
            )
        
        # Passa para o serviço de análise
        result = analyze_service.analyze_cnis(content)
        
        return AnalyzeResponse(
            status=result.get("status", "error"),
            message=result.get("message", "Erro desconhecido"),
            result=result.get("result")
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Erro ao processar arquivo: {str(e)}"
        )