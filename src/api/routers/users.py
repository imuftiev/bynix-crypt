from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from psycopg import Connection

from src.core.db import get_connection
from src.schemas.user import UserCreate


router = APIRouter(prefix="/user")


@router.post("/", status_code=HTTPStatus.CREATED, tags=["User create operation"])
async def create_user(user: UserCreate,
                      conn: Annotated[Connection,
                      Depends(get_connection)]
                      ) -> UserCreate:
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO users (user_id, username, password) VALUES (%s ,%s, %s)
        """,
        (user.user_id, user.username, user.password)
    )
    conn.commit()
    cursor.close()
    return user

@router.get("/", status_code=HTTPStatus.OK)
async def get_user(conn: Annotated[Connection,
                   Depends(get_connection)]) -> None:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.commit()
    return rows