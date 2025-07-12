from typing import Optional
from pydantic import BaseModel, ConfigDict
from .usuario import UsuarioInDB

class ColaboradorBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    cedula: str
    especialidad: str
    contacto: Optional[str] = None
    horario_atencion: Optional[str] = None

class ColaboradorCreate(ColaboradorBase):
    usuario_id: int

class ColaboradorUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    especialidad: Optional[str] = None
    contacto: Optional[str] = None
    horario_atencion: Optional[str] = None

class ColaboradorInDB(ColaboradorBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    usuario_id: int
    usuario: UsuarioInDB

