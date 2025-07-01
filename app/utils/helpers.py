import random
import string
from datetime import datetime, timedelta
from typing import Optional

def generate_verification_code(length: int = 16) -> str:
    """Genera un código alfanumérico aleatorio para verificación"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def format_datetime(dt: datetime) -> Optional[str]:
    """Formatea datetime a string ISO8601"""
    return dt.isoformat() if dt else None

def calculate_end_time(start_time: datetime, duration_minutes: int) -> datetime:
    """Calcula hora de fin basada en duración"""
    return start_time + timedelta(minutes=duration_minutes)

def validate_cedula(cedula: str) -> bool:
    """Valida formato básico de cédula (Ecuador)"""
    return len(cedula) == 10 and cedula.isdigit()