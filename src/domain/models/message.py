import uuid

from sqlalchemy import ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.domain.config.base import Base


class Message(Base):

    __tablename__ = "messages"

    message_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    message_content: Mapped[str]
    user_id: Mapped[uuid.UUID] = ForeignKey("users.user_id")
