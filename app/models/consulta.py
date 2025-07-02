from sqlalchemy import Column, Text, DateTime, ForeignKey, LargeBinary, String  # Asegúrate de importar String
from sqlalchemy.orm import relationship
from .base import Base  # Importa tu clase Base personalizada

class Consulta(Base):
    __tablename__ = "consultas"
    
    cita_id = Column(ForeignKey("citas.id"), nullable=False)
    colaborador_id = Column(ForeignKey("colaboradores.id"), nullable=False)
    diagnostico = Column(Text)
    evolucion = Column(Text)
    prescripciones = Column(Text)
    ordenes_medicas = Column(Text)
    fecha_consulta = Column(DateTime)
    version = Column(String(20))  # Longitud recomendada para campos de versión
    observaciones = Column(Text)
    resultados_clinicos_anexos = Column(LargeBinary)
    imagenes_medicas_anexas = Column(LargeBinary)
    
    # Relaciones
    cita = relationship("Cita", back_populates="consulta")
    colaborador = relationship("Colaborador", back_populates="consultas")
    certificados = relationship("Certificado", back_populates="consulta")