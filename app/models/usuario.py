from sqlalchemy import Column, String, Boolean, DateTime
from .base import Base
from sqlalchemy.sql import func

class Usuario(Base):
    __tablename__ = "usuarios"
    
    nombre_usuario = Column(String, unique=True, index=True, nullable=False)
    contrasena = Column(String, nullable=False)
    correo_electronico = Column(String, unique=True, index=True, nullable=False)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    ultimo_acceso = Column(DateTime(timezone=True))
    activo = Column(Boolean, default=True)
    es_administrador = Column(Boolean, default=False)
    es_colaborador = Column(Boolean, default=False)
    es_paciente = Column(Boolean, default=False)