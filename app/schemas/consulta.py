from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .cita import CitaInDB
from .colaborador import ColaboradorInDB

class ConsultaBase(BaseModel):
    diagnostico: Optional[str] = None
    evolucion: Optional[str] = None
    prescripciones: Optional[str] = None
    ordenes_medicas: Optional[str] = None
    fecha_consulta: Optional[datetime] = None
    observaciones: Optional[str] = None

class ConsultaCreate(ConsultaBase):
    cita_id: int
    colaborador_id: int

class ConsultaUpdate(BaseModel):
    diagnostico: Optional[str] = None
    evolucion: Optional[str] = None
    prescripciones: Optional[str] = None
    ordenes_medicas: Optional[str] = None
    observaciones: Optional[str] = None

class ConsultaInDB(ConsultaBase):
    id: int
    cita_id: int
    colaborador_id: int
    cita: CitaInDB
    colaborador: ColaboradorInDB
    version: str

    class Config:
        from_attributes = True