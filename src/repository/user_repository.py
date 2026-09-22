from typing import Annotated
from fastapi.params import Depends
from psycopg import AsyncConnection
from psycopg.rows import dict_row

from src.api.exceptions import UserAlreadyExists
from src.core.db import get_async_connection
from src.schemas.user import UserCreate


class UserRepository:

    def __init__(self, conn: AsyncConnection):
        self.conn = conn

    async def create(self, user: UserCreate) -> dict:
        try:
            async with self.conn.cursor(row_factory=dict_row) as cursor:
                await cursor.execute(
                    """
                    INSERT INTO users (user_id, username, password, email)
                    VALUES (%s, %s, %s, %s)
                        RETURNING username
                    """,
                    (
                        user.user_id,
                        user.username,
                        user.password,
                        user.email,
                    ),
                )
                result = await cursor.fetchone()
                await self.conn.commit()
                return result
        except Exception as e:
            print(e)
            raise UserAlreadyExists

    async def get(self, username: str) -> dict:
        try:
            async with self.conn.cursor(row_factory=dict_row) as cursor:
                await cursor.execute(
                    """
                    SELECT username, email FROM users WHERE username = %s 
                    """, (username,)
                )
                return await cursor.fetchone()
        except Exception as e:
            print(e)
            raise

def get_user_repository(conn: Annotated[AsyncConnection, Depends(get_async_connection)]) -> UserRepository:
    return UserRepository(conn)

