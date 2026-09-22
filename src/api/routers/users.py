from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from src.api.exceptions import UserAlreadyExists
from src.services.user_service import UserService, get_user_service
from src.schemas.user import to_response
from src.schemas.user import UserResponse, UserCreate

router = APIRouter(prefix="/user")


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    tags=["User create operation"],
    response_model=UserResponse,
)
async def create_user(
    user: UserCreate,
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserResponse:
    try:
        result = await service.create_user(user)
        return to_response(result)

    except UserAlreadyExists as e:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail=str(e),
        )

@router.get(
    "/{username}",
    status_code=HTTPStatus.OK,
    tags=["User get operation"]
)
async def get_user(
        username: str,
        service: Annotated[UserService, Depends(get_user_service)]
) -> UserResponse:
    try:
        result = await service.get_user(username)
        return result
    except Exception as e:
        print(e)