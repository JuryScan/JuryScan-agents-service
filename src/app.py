from fastapi import FastAPI
from dotenv import load_dotenv

from .routes import base_router, analyze_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="JuryScan Agents Service",
    description="Service for managing AI agents in the JuryScan system",
    version="1.0.0"
)

# CORS config (via middleware)
# routes
base_prefix = "/api/v1"
app.include_router(base_router, prefix=base_prefix)
app.include_router(analyze_router, prefix=base_prefix)