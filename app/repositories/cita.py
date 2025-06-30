from datetime import datetime
from sqlalchemy.orm import Session
from app.models.cita import Cita
from app.schemas.cita import CitaCreate, CitaUpdate
from app.repositories.base import CRUDBase
from ..utils.enums import EstadoCita

class CRUDCita(CRUDBase[Cita, CitaCreate, CitaUpdate]):
    def get_by_paciente(self, db: Session, paciente_id: int) -> list[Cita]:
        return db.query(Cita).filter(Cita.paciente_id == paciente_id).all()
    
    def get_by_colaborador(self, db: Session, colaborador_id: int) -> list[Cita]:
        return db.query(Cita).filter(Cita.colaborador_id == colaborador_id).all()
    
    def get_by_fecha(self, db: Session, fecha_inicio: datetime, fecha_fin: datetime) -> list[Cita]:
        return db.query(Cita).filter(
            Cita.fecha_hora >= fecha_inicio,
            Cita.fecha_hora <= fecha_fin
        ).all()
    
    def get_disponibles(self, db: Session, colaborador_id: int, fecha: datetime) -> list[Cita]:
        return db.query(Cita).filter(
            Cita.colaborador_id == colaborador_id,
            Cita.fecha_hora >= fecha,
            Cita.estado == EstadoCita.SOLICITADA
        ).all()

cita_repo = CRUDCita(Cita)