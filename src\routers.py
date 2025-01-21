import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

logger = logging.getLogger("uvicorn")


@router.get("/api/health-check")
async def health_check():
    """
    Health check endpoint
    """
    return JSONResponse({"status": "ok"})


@router.get("/api/hello-word")
async def hello_word():
    """
    Hello word endpoint
    """
    return "Hello word"