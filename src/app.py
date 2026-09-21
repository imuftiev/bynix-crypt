from fastapi import FastAPI
from src.domain.handlers.user import router

app = FastAPI()


app.include_router(router=router)