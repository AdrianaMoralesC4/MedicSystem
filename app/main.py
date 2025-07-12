from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import v1_router
from app.core.database import engine, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # ✅ Compatibilidad SQLAlchemy async
    print("✅ Base de datos inicializada")
    yield
    await engine.dispose()
    print("❌ Recursos liberados")

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Sistema de Gestión de Citas Médicas - API",
        version="1.0.0",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        lifespan=lifespan
    )
    app.include_router(v1_router)
    return app

app = create_app()

