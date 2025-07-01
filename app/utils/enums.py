from enum import Enum

class EstadoCita(str, Enum):
    """Estados posibles de una cita médica"""
    SOLICITADA = "SOLICITADA"
    CONFIRMADA = "CONFIRMADA"
    ATENDIDA = "ATENDIDA"
    FINALIZADA = "FINALIZADA"
    CANCELADA = "CANCELADA"
    RECHAZADA = "RECHAZADA"

class TipoCertificado(str, Enum):
    """Tipos de certificados médicos"""
    ASISTENCIA = "ASISTENCIA"
    REPOSO = "REPOSO"
    SALUD = "SALUD"
    OTRO = "OTRO"

class TipoReporte(str, Enum):
    """Tipos de reportes del sistema"""
    MEDICO = "MEDICO"
    FINANCIERO = "FINANCIERO"
    USUARIOS = "USUARIOS"