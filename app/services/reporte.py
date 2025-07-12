from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.schemas.reporte import ReporteCreate, ReporteUpdate, ReporteInDB
from app.repositories.reporte import reporte_repo
from app.services.base import ServiceBase

class ReporteService(ServiceBase[ReporteInDB, ReporteCreate, ReporteUpdate]):
    def __init__(self):
        super().__init__(reporte_repo)

    def create(self, db: Session, obj_in: ReporteCreate) -> ReporteInDB:
        # Añadir fecha_creacion automáticamente
        data = obj_in.model_dump()
        data["fecha_creacion"] = datetime.now(timezone.utc)
        obj_in_with_fecha = ReporteCreate(**data)
        return super().create(db, obj_in=obj_in_with_fecha)

    def get_by_tipo(self, db: Session, tipo: str) -> list[ReporteInDB]:
        return reporte_repo.get_by_tipo(db, tipo=tipo.upper())

    def get_by_usuario(self, db: Session, usuario_id: int) -> list[ReporteInDB]:
        return reporte_repo.get_by_usuario(db, usuario_id=usuario_id)

    def generar_reporte_medico(self, db: Session, filtros: dict, usuario_id: int) -> ReporteInDB:
        reporte_data = {
            "tipo_reporte": "MEDICO",
            "filtros_aplicados": str(filtros),
            "formato_exportacion": "PDF",
            "usuario_id": usuario_id
        }
        return self.create(db, ReporteCreate(**reporte_data))

    def generar_reporte_financiero(self, db: Session, filtros: dict, usuario_id: int) -> ReporteInDB:
        reporte_data = {
            "tipo_reporte": "FINANCIERO",
            "filtros_aplicados": str(filtros),
            "formato_exportacion": "Excel",
            "usuario_id": usuario_id
        }
        return self.create(db, ReporteCreate(**reporte_data))

reporte_service = ReporteService()



