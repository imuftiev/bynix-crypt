from fastapi import APIRouter


router = APIRouter(prefix="/message", tags=["Messages"])

@router.get("/")
async def get_message() -> None:
    pass

@router.post("/")
async def create_message() -> None:
    pass

@router.put("/")
async def update_message() -> None:
    pass

@router.delete("/")
async def delete_message() -> None:
    pass