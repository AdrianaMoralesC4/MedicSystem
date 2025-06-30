from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.reporte import ReporteInDB
from app.schemas.usuario import UsuarioInDB  # Importación clave
from app.core.security import get_current_admin_user  # Función específica para admin
from app.services.reporte import reporte_service
from app.core.database import get_db

router = APIRouter(prefix="/reportes")

@router.post("/medicos", response_model=ReporteInDB)
def generar_reporte_medico(
    filtros: dict,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_admin_user)  # Correcto
):
    """
    Genera reporte médico (solo administradores)
    """
    return reporte_service.generar_reporte_medico(db, filtros, current_user.id)

@router.post("/financieros", response_model=ReporteInDB)
def generar_reporte_financiero(
    filtros: dict,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_admin_user)  # Correcto
):
    """
    Genera reporte financiero (solo administradores)
    """
    return reporte_service.generar_reporte_financiero(db, filtros, current_user.id)