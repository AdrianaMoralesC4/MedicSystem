from fastapi import APIRouter
from .usuarios import router as usuarios_router
from .pacientes import router as pacientes_router
from .colaboradores import router as colaboradores_router
from .citas import router as citas_router
from .consultas import router as consultas_router
from .certificados import router as certificados_router
from .reportes import router as reportes_router
from app.core.config import settings

api_router = APIRouter(prefix=settings.API_V1_STR)

# Integración de todos los routers
api_router.include_router(
    usuarios_router,
    prefix="/usuarios",
    tags=["Usuarios"]
)
api_router.include_router(
    pacientes_router,
    prefix="/pacientes",
    tags=["Pacientes"]
)
api_router.include_router(
    colaboradores_router,
    prefix="/colaboradores",
    tags=["Colaboradores"]
)
api_router.include_router(
    citas_router,
    prefix="/citas",
    tags=["Citas Médicas"]
)
api_router.include_router(
    consultas_router,
    prefix="/consultas",
    tags=["Consultas Médicas"]
)
api_router.include_router(
    certificados_router,
    prefix="/certificados",
    tags=["Certificados Médicos"]
)
api_router.include_router(
    reportes_router,
    prefix="/reportes",
    tags=["Reportes"]
)