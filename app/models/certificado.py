from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from .base import Base

class Certificado(Base):
    __tablename__ = "certificados"
    
    consulta_id = Column(ForeignKey("consultas.id"), nullable=False)
    colaborador_id = Column(ForeignKey("colaboradores.id"), nullable=False)
    tipo_certificado = Column(String, nullable=False)
    codigo_verificacion = Column(String, unique=True, nullable=False)
    fecha_emision = Column(DateTime, nullable=False)
    contenido = Column(Text, nullable=False)
    
    consulta = relationship("Consulta", back_populates="certificados")
    colaborador = relationship("Colaborador", back_populates="certificados")