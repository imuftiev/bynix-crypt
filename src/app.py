from fastapi import FastAPI
from src.api.routers.users import router
from src.core.base import Base

app = FastAPI()


app.include_router(router=router)