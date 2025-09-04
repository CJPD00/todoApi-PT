# ensure_database.py
import asyncio
import asyncpg
from app.core.config import settings


async def create_db():
    conn = await asyncpg.connect(
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        database="postgres",  # conectamos a la base por defecto
    )
    db_exists = await conn.fetchval(
        "SELECT 1 FROM pg_database WHERE datname = $1", settings.POSTGRES_DB
    )
    if not db_exists:
        await conn.execute(f'CREATE DATABASE "{settings.POSTGRES_DB}"')
        print(f"✅ Base de datos '{settings.POSTGRES_DB}' creada.")
    else:
        print(f"ℹ️ Base de datos '{settings.POSTGRES_DB}' ya existe.")
    await conn.close()


if __name__ == "__main__":
    asyncio.run(create_db())
