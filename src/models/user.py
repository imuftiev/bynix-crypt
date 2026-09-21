import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(
        unique=True
    )

    password: Mapped[str]

    messages = relationship("messages")