from typing import Optional
from pydantic import BaseModel
from .usuario import UsuarioInDB

class ColaboradorBase(BaseModel):
    cedula: str
    especialidad: str
    contacto: Optional[str] = None
    horario_atencion: Optional[str] = None

class ColaboradorCreate(ColaboradorBase):
    usuario_id: int

class ColaboradorUpdate(BaseModel):
    especialidad: Optional[str] = None
    contacto: Optional[str] = None
    horario_atencion: Optional[str] = None

class ColaboradorInDB(ColaboradorBase):
    id: int
    usuario_id: int
    usuario: UsuarioInDB

    class Config:
        from_attributes = True