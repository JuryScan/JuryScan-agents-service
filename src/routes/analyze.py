from fastapi import APIRouter
from ..schemas import AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.post("/analyze")
async def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    return AnalyzeResponse("placeholder")