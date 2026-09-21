import uuid
from pydantic import Field
from uuid import UUID
from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: UUID = Field(default_factory=uuid.uuid4)
    username: str
    password: str
