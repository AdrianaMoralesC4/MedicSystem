from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.repositories.base import CRUDBase
from app.core.password import verify_password, get_password_hash  # Importar las funciones de seguridad

class CRUDUsuario(CRUDBase[Usuario, UsuarioCreate, UsuarioUpdate]):
    def get_by_email(self, db: Session, email: str) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.correo_electronico == email).first()
    
    def get_by_username(self, db: Session, username: str) -> Usuario | None:
        return db.query(Usuario).filter(Usuario.nombre_usuario == username).first()
    
    def create(self, db: Session, obj_in: UsuarioCreate) -> Usuario:
        db_obj = Usuario(
            nombre_usuario=obj_in.nombre_usuario,
            correo_electronico=obj_in.correo_electronico,
            contrasena=get_password_hash(obj_in.contrasena),  # Usar get_password_hash
            activo=True
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def authenticate(self, db: Session, username: str, password: str) -> Usuario | None:
        usuario = self.get_by_username(db, username=username)
        if not usuario:
            return None
        if not verify_password(password, usuario.contrasena):  # Ahora funciona
            return None
        return usuario

usuario_repo = CRUDUsuario(Usuario)