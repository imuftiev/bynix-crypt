from typing import Annotated

from fastapi import Depends

from src.repository.user_repository import UserRepository, get_user_repository
from src.schemas.user import UserCreate, to_response, UserResponse


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, user: UserCreate) -> dict:
        return await self.repository.create(user)

    async def get_user(self, username: str) -> dict:
        return await self.repository.get(username)


def get_user_service(repository: Annotated[
    UserRepository,
    Depends(get_user_repository)
]) -> UserService:
    return UserService(repository)