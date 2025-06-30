from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioInDB
from app.core.security import get_current_admin_user
from app.services.usuario import usuario_service
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=UsuarioInDB)
def create_user(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_admin_user)
):
    return usuario_service.create(db, obj_in=usuario)

@router.get("/{user_id}", response_model=UsuarioInDB)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_admin_user)
):
    return usuario_service.get(db, id=user_id)