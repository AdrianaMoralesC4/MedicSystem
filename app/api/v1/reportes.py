from fastapi import APIRouter, Depends, HTTPException, Body, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_admin_user
from app.schemas.reporte import ReporteInDB
from app.services.reporte import reporte_service
from typing import List

# ✅ Quitamos el prefix redundante
router = APIRouter(tags=["reportes"])

@router.get("/", response_model=List[ReporteInDB])
def listar_reportes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return reporte_service.get_multi(db, skip=skip, limit=limit)

@router.post("/medicos", response_model=ReporteInDB, status_code=status.HTTP_201_CREATED)
def generar_reporte_medico(
    filtros: dict,
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_admin_user)
):
    return reporte_service.generar_reporte_medico(
        db,
        filtros=filtros,
        usuario_id=current_admin.id  # ✅ usamos .id porque es un objeto Usuario
    )



