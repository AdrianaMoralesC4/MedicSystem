from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.cita import CitaCreate, CitaInDB
from app.schemas.usuario import UsuarioInDB
from app.core.security import get_current_active_user
from app.services.cita import cita_service
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=CitaInDB, status_code=201)
def create_cita(
    cita: CitaCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)
):
    # Solo paciente dueño o admin pueden agendar citas
    if not (current_user.es_administrador or current_user.es_paciente):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo pacientes o administradores pueden agendar citas"
        )
    return cita_service.create(db, obj_in=cita)


@router.get("/{cita_id}", response_model=CitaInDB)
def read_cita(
    cita_id: int,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)
):
    return cita_service.get(db, id=cita_id)

