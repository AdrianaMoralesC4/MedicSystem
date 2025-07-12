from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, constr
from .usuario import UsuarioInDB

class ReporteBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo_reporte: constr(strip_whitespace=True, to_upper=True)  # Siempre en mayúsculas
    filtros_aplicados: Optional[str] = None
    formato_exportacion: Optional[str] = None

class ReporteCreate(ReporteBase):
    usuario_id: int
    fecha_creacion: Optional[datetime] = None  # <-- AGREGADO

class ReporteUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo_reporte: Optional[constr(strip_whitespace=True, to_upper=True)] = None
    filtros_aplicados: Optional[str] = None
    formato_exportacion: Optional[str] = None
    usuario_id: Optional[int] = None

class ReporteInDB(ReporteBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    usuario_id: int
    fecha_creacion: datetime
    usuario: UsuarioInDB



