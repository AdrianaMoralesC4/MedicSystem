# Importa el router principal de la API v1
from .v1 import api_router as v1_router

__all__ = [
    'v1_router'
]