from typing import Optional
from pydantic import BaseModel, ConfigDict
from .usuario import UsuarioInDB

class PacienteBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombres: str
    cedula: str
    contacto: Optional[str] = None
    direccion: Optional[str] = None
    datos_facturacion: Optional[str] = None

class PacienteCreate(PacienteBase):
    usuario_id: int

class PacienteUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombres: Optional[str] = None
    contacto: Optional[str] = None
    direccion: Optional[str] = None
    datos_facturacion: Optional[str] = None

class PacienteInDB(PacienteBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    usuario_id: int
    usuario: UsuarioInDB
