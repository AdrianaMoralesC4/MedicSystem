from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .base import BaseSchema

class UsuarioBase(BaseSchema):
    nombre_usuario: str
    correo_electronico: str

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioUpdate(BaseSchema):
    nombre_usuario: Optional[str] = None
    correo_electronico: Optional[str] = None
    contrasena: Optional[str] = None
    activo: Optional[bool] = None

class UsuarioInDB(UsuarioBase):
    id: int
    fecha_registro: datetime
    ultimo_acceso: Optional[datetime]
    activo: bool
    es_administrador: bool
    es_colaborador: bool
    es_paciente: bool

    class Config:
        from_attributes = True