from typing import Optional
from pydantic import BaseModel
from .usuario import UsuarioInDB

class PacienteBase(BaseModel):
    nombres: str
    cedula: str
    contacto: Optional[str] = None
    direccion: Optional[str] = None
    datos_facturacion: Optional[str] = None

class PacienteCreate(PacienteBase):
    usuario_id: int

class PacienteUpdate(BaseModel):
    nombres: Optional[str] = None
    contacto: Optional[str] = None
    direccion: Optional[str] = None
    datos_facturacion: Optional[str] = None

class PacienteInDB(PacienteBase):
    id: int
    usuario_id: int
    usuario: UsuarioInDB

    class Config:
        from_attributes = True