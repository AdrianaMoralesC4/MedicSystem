from sqlalchemy.orm import Session
from app.models.consulta import Consulta
from app.schemas.consulta import ConsultaCreate, ConsultaUpdate
from app.repositories.base import CRUDBase

class CRUDConsulta(CRUDBase[Consulta, ConsultaCreate, ConsultaUpdate]):
    def get_by_cita(self, db: Session, cita_id: int) -> Consulta | None:
        return db.query(Consulta).filter(Consulta.cita_id == cita_id).first()
    
    def get_by_colaborador(self, db: Session, colaborador_id: int) -> list[Consulta]:
        return db.query(Consulta).filter(Consulta.colaborador_id == colaborador_id).all()

consulta_repo = CRUDConsulta(Consulta)