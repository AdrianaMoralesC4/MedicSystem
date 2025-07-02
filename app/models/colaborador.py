from sqlalchemy import Column, String, Text, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .base import Base
from .usuario import Usuario

class Colaborador(Base):
    __tablename__ = "colaboradores"
    
    usuario_id = Column(ForeignKey("usuarios.id"), nullable=False)
    cedula = Column(String, unique=True, nullable=False)
    contacto = Column(String)
    especialidad = Column(String, nullable=False)
    horario_atencion = Column(String)
    firma_digital = Column(LargeBinary)
    documentos_adjuntos = Column(Text)
    
    usuario = relationship("Usuario")
    citas = relationship("Cita", back_populates="colaborador")
    consultas = relationship("Consulta", back_populates="colaborador")
    certificados = relationship("Certificado", back_populates="colaborador")