from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base

class Reporte(Base):
    __tablename__ = "reportes"
    
    usuario_id = Column(ForeignKey("usuarios.id"), nullable=False)
    tipo_reporte = Column(String, nullable=False)
    fecha_creacion = Column(DateTime, nullable=False)
    filtros_aplicados = Column(Text)
    formato_exportacion = Column(String)
    
    usuario = relationship("Usuario")