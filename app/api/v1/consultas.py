from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.consulta import ConsultaCreate, ConsultaInDB
from app.schemas.usuario import UsuarioInDB
from app.core.security import get_current_active_user
from app.services.consulta import consulta_service
from app.core.database import get_db

router = APIRouter(prefix="/consultas")

@router.post("/", response_model=ConsultaInDB)
def create_consulta(
    consulta: ConsultaCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)
):
    """
    Crear una nueva consulta médica.
    Requiere ser colaborador de salud.
    """
    if not current_user.es_colaborador:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo colaboradores de salud pueden registrar consultas"
        )
    
    return consulta_service.create(db, obj_in=consulta)

@router.get("/{consulta_id}", response_model=ConsultaInDB)
def read_consulta(
    consulta_id: int,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)
):
    """
    Obtener detalles de una consulta específica.
    """
    consulta = consulta_service.get(db, id=consulta_id)
    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consulta no encontrada"
        )
    
    # Verificar permisos (médico o paciente relacionado)
    if not (current_user.es_colaborador or current_user.id == consulta.cita.paciente.usuario_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para ver esta consulta"
        )
    
    return consulta