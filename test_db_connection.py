import asyncio
import asyncpg
from app.core.config import settings


async def test_connection():
    try:

        conn = await asyncpg.connect(
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            database=settings.POSTGRES_DB,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
        )
        print("✅ Conexión exitosa a PostgreSQL")
        await conn.close()
    except Exception as e:
        print("❌ Error de conexión:", e)


if __name__ == "__main__":
    asyncio.run(test_connection())
