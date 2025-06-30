from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .usuario import UsuarioInDB

class ReporteBase(BaseModel):
    tipo_reporte: str
    filtros_aplicados: Optional[str] = None
    formato_exportacion: Optional[str] = None

class ReporteCreate(ReporteBase):
    usuario_id: int

class ReporteUpdate(BaseModel):
    tipo_reporte: Optional[str] = None
    filtros_aplicados: Optional[str] = None
    formato_exportacion: Optional[str] = None
    usuario_id: Optional[int] = None

class ReporteInDB(ReporteBase):
    id: int
    usuario_id: int
    fecha_creacion: datetime
    usuario: UsuarioInDB

    class Config:
        from_attributes = True