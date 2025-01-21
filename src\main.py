import logging

from fastapi import FastAPI

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

from src.routers import router

app = FastAPI()


app.include_router(router)