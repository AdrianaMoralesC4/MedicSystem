from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.paciente import PacienteCreate, PacienteInDB
from app.schemas.usuario import UsuarioInDB  # Importación clave
from app.core.security import get_current_active_user
from app.services.paciente import paciente_service
from app.core.database import get_db

router = APIRouter(prefix="/pacientes")

@router.post("/", response_model=PacienteInDB)
def create_paciente(
    paciente: PacienteCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)  # Correcto
):
    """
    Registrar un nuevo paciente.
    Requiere autenticación.
    """
    # Verificar permisos (ej: solo administradores o el propio usuario)
    if not current_user.es_administrador:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requieren privilegios de administrador"
        )
    
    return paciente_service.create(db, obj_in=paciente)

@router.get("/{paciente_id}", response_model=PacienteInDB)
def read_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)
):
    """
    Obtener información de un paciente específico.
    """
    paciente = paciente_service.get(db, id=paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    
    # Verificar que el usuario tenga permisos
    if not (current_user.es_administrador or current_user.id == paciente.usuario_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No autorizado para ver este paciente"
        )
    
    return paciente