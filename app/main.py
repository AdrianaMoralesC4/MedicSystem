from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import v1_router
from app.core.database import engine, Base

def create_app() -> FastAPI:
    # Crear instancia de FastAPI con metadatos
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Sistema de Gestión de Citas Médicas - API",
        version="1.0.0",
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # 1. Añadir middleware CORS (Corrección crítica #2)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # En producción, reemplazar con dominios específicos
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 2. Eventos de ciclo de vida (Corrección implícita para DB)
    @app.on_event("startup")
    async def startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Base de datos inicializada")

    @app.on_event("shutdown")
    async def shutdown():
        await engine.dispose()
        print("❌ Recursos liberados")

    # 3. Incluir router (Corrección #3 - asegura carga adecuada)
    def include_routers():
        app.include_router(v1_router)

    include_routers()  # Llama explícitamente para evitar imports circulares

    return app

app = create_app()