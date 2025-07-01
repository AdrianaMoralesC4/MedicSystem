from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioInDB
from app.repositories.usuario import usuario_repo
from app.services.base import ServiceBase
from app.core.database import get_db
from app.core.security import get_password_hash, verify_password

class UsuarioService(ServiceBase[UsuarioInDB, UsuarioCreate, UsuarioUpdate]):
    def __init__(self):
        super().__init__(usuario_repo)
    
    def authenticate(self, db: Session, username: str, password: str) -> UsuarioInDB | None:
        usuario = self.repository.authenticate(db, username=username, password=password)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return usuario
    
    def create(self, db: Session, obj_in: UsuarioCreate) -> UsuarioInDB:
        if self.repository.get_by_username(db, username=obj_in.nombre_usuario):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre de usuario ya existe",
            )
        if self.repository.get_by_email(db, email=obj_in.correo_electronico):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico ya está registrado",
            )
        return super().create(db, obj_in=obj_in)

usuario_service = UsuarioService()