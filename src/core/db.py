import psycopg
from psycopg import Connection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

DATABASE_URL="postgresql+asyncpg://admin_ilyas:1234@localhost:5432/bynix"
async_engine = create_async_engine(DATABASE_URL)
async_sessionmaker = async_sessionmaker(bind=async_engine)

async def get_session():
    async with AsyncSession(async_engine) as session:
        yield session

async def get_connection() -> Connection:
    connection = psycopg.connect("postgresql://admin_ilyas:12345@localhost:5432/bynix")
    return connection

