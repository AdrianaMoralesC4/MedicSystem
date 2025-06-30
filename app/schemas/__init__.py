from .base import BaseSchema
from .usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate, UsuarioInDB
from .paciente import PacienteBase, PacienteCreate, PacienteUpdate, PacienteInDB
from .colaborador import ColaboradorBase, ColaboradorCreate, ColaboradorUpdate, ColaboradorInDB
from .cita import CitaBase, CitaCreate, CitaUpdate, CitaInDB
from .consulta import ConsultaBase, ConsultaCreate, ConsultaUpdate, ConsultaInDB
from .certificado import CertificadoBase, CertificadoCreate, CertificadoInDB
from .reporte import ReporteBase, ReporteCreate, ReporteInDB

__all__ = [
    'BaseSchema',
    'UsuarioBase', 'UsuarioCreate', 'UsuarioUpdate', 'UsuarioInDB',
    'PacienteBase', 'PacienteCreate', 'PacienteUpdate', 'PacienteInDB',
    'ColaboradorBase', 'ColaboradorCreate', 'ColaboradorUpdate', 'ColaboradorInDB',
    'CitaBase', 'CitaCreate', 'CitaUpdate', 'CitaInDB',
    'ConsultaBase', 'ConsultaCreate', 'ConsultaUpdate', 'ConsultaInDB',
    'CertificadoBase', 'CertificadoCreate', 'CertificadoInDB',
    'ReporteBase', 'ReporteCreate', 'ReporteInDB'
]