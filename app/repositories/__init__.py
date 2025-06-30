from .base import CRUDBase
from .usuario import usuario_repo
from .paciente import paciente_repo
from .colaborador import colaborador_repo
from .cita import cita_repo
from .consulta import consulta_repo
from .certificado import certificado_repo
from .reporte import reporte_repo

__all__ = [
    'CRUDBase',
    'usuario_repo',
    'paciente_repo',
    'colaborador_repo',
    'cita_repo',
    'consulta_repo',
    'certificado_repo',
    'reporte_repo'
]