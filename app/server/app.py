from fastapi import FastAPI
from app.routers import chat_completions
from app.config import API_V1

app = FastAPI()

app.include_router(chat_completions.router, prefix=API_V1)