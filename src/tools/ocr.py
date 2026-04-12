"""Ferramentas de OCR e extração de texto de documentos"""
import io
import base64
import pdfplumber
from crewai.tools import tool

@tool
def tool_extract_text_from_pdf(pdf_content_base64: str) -> str:
    """
    Extrai texto de um arquivo PDF recebido em formato base64, retornando o conteúdo extraído como string.
    """
    try:
        # Decodifica base64 para bytes
        pdf_bytes = base64.b64decode(pdf_content_base64)
        
        # Extrai texto do PDF
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            text = ""
            for page_num, page in enumerate(pdf.pages, 1):
                extracted = page.extract_text()
                if extracted:
                    text += f"\n--- Página {page_num} ---\n{extracted}"
            return text if text.strip() else "Nenhum texto encontrado no PDF"
    
    except Exception as e:
        return f"Erro ao extrair texto do PDF: {str(e)}"