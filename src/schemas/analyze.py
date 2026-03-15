from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    def __init__(self, text: str):
        self.text = text

class AnalyzeResponse(BaseModel):
    def __init__(self, response: str):
        self.response = response