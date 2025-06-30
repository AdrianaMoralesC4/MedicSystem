from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.colaborador import ColaboradorCreate, ColaboradorInDB
from app.schemas.usuario import UsuarioInDB  # Importación explícita
from app.core.security import get_current_active_user
from app.services.colaborador import colaborador_service
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=ColaboradorInDB)
def create_colaborador(
    colaborador: ColaboradorCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)  # Uso correcto
):
    # Verificar permisos
    if not current_user.es_administrador:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo administradores pueden crear colaboradores"
        )
    
    return colaborador_service.create(db, obj_in=colaborador)