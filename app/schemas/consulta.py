from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from .cita import CitaInDB
from .colaborador import ColaboradorInDB

class ConsultaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    diagnostico: Optional[str] = None
    evolucion: Optional[str] = None
    prescripciones: Optional[str] = None
    ordenes_medicas: Optional[str] = None
    fecha_consulta: Optional[datetime] = None
    observaciones: Optional[str] = None
    version: Optional[str] = None

class ConsultaCreate(ConsultaBase):
    cita_id: int
    colaborador_id: int

class ConsultaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    diagnostico: Optional[str] = None
    evolucion: Optional[str] = None
    prescripciones: Optional[str] = None
    ordenes_medicas: Optional[str] = None
    observaciones: Optional[str] = None
    version: Optional[str] = None

class ConsultaInDB(ConsultaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    cita_id: int
    colaborador_id: int
    cita: CitaInDB
    colaborador: ColaboradorInDB



