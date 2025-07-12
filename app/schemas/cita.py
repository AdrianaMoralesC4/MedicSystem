from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from ..utils.enums import EstadoCita
from .paciente import PacienteInDB
from .colaborador import ColaboradorInDB

class CitaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fecha_hora: datetime
    estado: EstadoCita = EstadoCita.SOLICITADA
    motivo: Optional[str] = None

class CitaCreate(CitaBase):
    paciente_id: int
    colaborador_id: int

class CitaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fecha_hora: Optional[datetime] = None
    estado: Optional[EstadoCita] = None
    motivo: Optional[str] = None

class CitaInDB(CitaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    paciente_id: int
    colaborador_id: int
    paciente: PacienteInDB
    colaborador: ColaboradorInDB

