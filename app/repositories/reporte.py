from sqlalchemy.orm import Session
from app.models.reporte import Reporte
from app.schemas.reporte import ReporteCreate, ReporteUpdate
from app.repositories.base import CRUDBase

class CRUDReporte(CRUDBase[Reporte, ReporteCreate, ReporteUpdate]):
    def get_by_tipo(self, db: Session, tipo: str) -> list[Reporte]:
        return db.query(Reporte).filter(Reporte.tipo_reporte == tipo).all()
    
    def get_by_usuario(self, db: Session, usuario_id: int) -> list[Reporte]:
        return db.query(Reporte).filter(Reporte.usuario_id == usuario_id).all()

reporte_repo = CRUDReporte(Reporte)