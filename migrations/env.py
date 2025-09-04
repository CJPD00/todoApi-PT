from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncConnection, create_async_engine
from alembic import context

from app.core.config import settings
from app.db.session import Base
from app.models import user, task  # Asegura que Alembic detecte los modelos

# Alembic config object
config = context.config

# Configuración de logging (solo si hay archivo definido)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Construye la URL de conexión desde settings
url = (
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)

# Metadata objetivo para autogenerar migraciones
target_metadata = Base.metadata


# Modo offline: genera SQL sin ejecutar
def run_migrations_offline() -> None:
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


# Modo online: ejecuta migraciones directamente
def run_migrations_online() -> None:
    connectable: AsyncEngine = create_async_engine(url, poolclass=pool.NullPool)

    async def do_run_migrations(connection: AsyncConnection) -> None:
        def sync_migrations(sync_conn):
            context.configure(
                connection=sync_conn,
                target_metadata=target_metadata,
                render_as_batch=True,  # útil para SQLite; puedes quitarlo si usas PostgreSQL
            )
            with context.begin_transaction():
                context.run_migrations()

        await connection.run_sync(sync_migrations)

    import asyncio

    async def run() -> None:
        async with connectable.connect() as connection:
            await do_run_migrations(connection)

    asyncio.run(run())


# Decide modo según contexto
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
