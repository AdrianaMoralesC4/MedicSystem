from sqlalchemy import Column, DateTime, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.utils.enums import EstadoCita  
from .base import Base

class Cita(Base):
    __tablename__ = "citas"
    
    paciente_id = Column(ForeignKey("pacientes.id"), nullable=False)
    colaborador_id = Column(ForeignKey("colaboradores.id"), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    estado = Column(Enum(EstadoCita), nullable=False, default=EstadoCita.SOLICITADA)
    motivo = Column(String)
    
    paciente = relationship("Paciente", back_populates="citas")
    colaborador = relationship("Colaborador", back_populates="citas")
    consulta = relationship("Consulta", back_populates="cita", uselist=False, cascade="all, delete-orphan")