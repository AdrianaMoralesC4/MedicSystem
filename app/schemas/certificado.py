from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from .consulta import ConsultaInDB
from .colaborador import ColaboradorInDB

class CertificadoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo_certificado: str
    codigo_verificacion: str
    fecha_emision: datetime
    contenido: str

# Cambiado: solo recibe los campos necesarios desde el cliente
class CertificadoCreate(BaseModel):
   consulta_id: int
   colaborador_id: int
   tipo_certificado: str
   contenido: str
   # Añadir campos generados como opcionales
   codigo_verificacion: Optional[str] = None
   fecha_emision: Optional[datetime] = None

class CertificadoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo_certificado: Optional[str] = None
    codigo_verificacion: Optional[str] = None
    fecha_emision: Optional[datetime] = None
    contenido: Optional[str] = None
    consulta_id: Optional[int] = None
    colaborador_id: Optional[int] = None

class CertificadoInDB(CertificadoBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    consulta_id: int
    colaborador_id: int
    consulta: ConsultaInDB
    colaborador: ColaboradorInDB

