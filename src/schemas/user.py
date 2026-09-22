import uuid
from pydantic import Field
from uuid import UUID
from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    user_id: UUID = Field(default_factory=uuid.uuid4)
    username: str = Field(max_length=10)
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: EmailStr

def to_response(user: dict) -> UserResponse:
    return UserResponse(
        username=user["username"],
        email=user["email"]
    )