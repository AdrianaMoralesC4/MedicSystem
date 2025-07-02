from sqlalchemy import Column, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .usuario import Usuario

class Paciente(Base):
    __tablename__ = "pacientes"
    
    usuario_id = Column(ForeignKey("usuarios.id"), nullable=False)
    nombres = Column(String, nullable=False)
    cedula = Column(String, unique=True, nullable=False)
    contacto = Column(String)
    direccion = Column(String)
    datos_facturacion = Column(Text)
    
    usuario = relationship("Usuario")
    citas = relationship("Cita", back_populates="paciente")