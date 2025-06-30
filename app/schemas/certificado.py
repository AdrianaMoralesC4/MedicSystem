from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .consulta import ConsultaInDB
from .colaborador import ColaboradorInDB

class CertificadoBase(BaseModel):
    tipo_certificado: str
    codigo_verificacion: str
    fecha_emision: datetime
    contenido: str

class CertificadoCreate(CertificadoBase):
    consulta_id: int
    colaborador_id: int

class CertificadoUpdate(BaseModel):
    tipo_certificado: Optional[str] = None
    codigo_verification: Optional[str] = None
    fecha_emision: Optional[datetime] = None
    contenido: Optional[str] = None
    consulta_id: Optional[int] = None
    colaborador_id: Optional[int] = None

class CertificadoInDB(CertificadoBase):
    id: int
    consulta_id: int
    colaborador_id: int
    consulta: ConsultaInDB
    colaborador: ColaboradorInDB

    class Config:
        from_attributes = True