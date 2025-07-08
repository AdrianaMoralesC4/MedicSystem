from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from .config import settings

# Asegúrate de que la URL sea la correcta
SQLALCHEMY_DATABASE_URL = settings.DB_URL

# Configura el motor asíncrono
print(f"DB URL: {SQLALCHEMY_DATABASE_URL}")  # ← Añade esto
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"server_settings": {"application_name": "my_app"}},
    pool_pre_ping=True,
    echo=True  # Habilita logs para debug
)

# Usa async_sessionmaker (no sessionmaker)
SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        yield db