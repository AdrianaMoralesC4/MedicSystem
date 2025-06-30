from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador
from app.schemas.colaborador import ColaboradorCreate, ColaboradorUpdate
from app.repositories.base import CRUDBase

class CRUDColaborador(CRUDBase[Colaborador, ColaboradorCreate, ColaboradorUpdate]):
    def get_by_cedula(self, db: Session, cedula: str) -> Colaborador | None:
        return db.query(Colaborador).filter(Colaborador.cedula == cedula).first()
    
    def get_by_especialidad(self, db: Session, especialidad: str) -> list[Colaborador]:
        return db.query(Colaborador).filter(Colaborador.especialidad == especialidad).all()

colaborador_repo = CRUDColaborador(Colaborador)