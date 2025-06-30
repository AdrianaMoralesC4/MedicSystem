from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate, PacienteUpdate
from app.repositories.base import CRUDBase

class CRUDPaciente(CRUDBase[Paciente, PacienteCreate, PacienteUpdate]):
    def get_by_cedula(self, db: Session, cedula: str) -> Paciente | None:
        return db.query(Paciente).filter(Paciente.cedula == cedula).first()

paciente_repo = CRUDPaciente(Paciente)