from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.schemas.consulta import ConsultaCreate, ConsultaUpdate, ConsultaInDB
from app.repositories.consulta import consulta_repo
from app.services.base import ServiceBase
from app.repositories.cita import cita_repo

class ConsultaService(ServiceBase[ConsultaInDB, ConsultaCreate, ConsultaUpdate]):
    def __init__(self):
        super().__init__(consulta_repo)
    
    def create(self, db: Session, obj_in: ConsultaCreate) -> ConsultaInDB:
        cita = cita_repo.get(db, id=obj_in.cita_id)
        if not cita:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La cita no existe")
        
        # Crear una copia con valores por defecto
        obj_in_data = obj_in.model_dump()
        if not obj_in_data.get("fecha_consulta"):
            obj_in_data["fecha_consulta"] = datetime.now(timezone.utc)
        obj_in_data["version"] = "1.0"
        
        return super().create(db, obj_in=ConsultaCreate(**obj_in_data))
    
    def update(self, db: Session, id: int, obj_in: ConsultaUpdate) -> ConsultaInDB:
        consulta = self.get(db, id=id)
        if not consulta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta no encontrada")
        
        # Verificar cambios para incrementar versión
        has_changes = any([
            obj_in.diagnostico is not None,
            obj_in.evolucion is not None,
            obj_in.prescripciones is not None,
            obj_in.ordenes_medicas is not None,
            obj_in.observaciones is not None
        ])
        new_version = consulta.version
        if has_changes and consulta.version:
            major, minor = map(int, consulta.version.split('.'))
            minor += 1
            new_version = f"{major}.{minor}"
        
        obj_in_data = obj_in.model_dump()
        obj_in_data["version"] = new_version
        
        return super().update(db, id=id, obj_in=ConsultaUpdate(**obj_in_data))
    
    def get_by_cita(self, db: Session, cita_id: int) -> ConsultaInDB:
        consulta = consulta_repo.get_by_cita(db, cita_id=cita_id)
        if not consulta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró consulta para esta cita")
        return consulta
    
    def get_by_colaborador(self, db: Session, colaborador_id: int) -> list[ConsultaInDB]:
        return consulta_repo.get_by_colaborador(db, colaborador_id=colaborador_id)

consulta_service = ConsultaService()


