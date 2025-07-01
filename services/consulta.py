from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from app.schemas.consulta import ConsultaCreate, ConsultaUpdate, ConsultaInDB
from app.repositories.consulta import consulta_repo
from app.services.base import ServiceBase
from app.repositories.cita import cita_repo

class ConsultaService(ServiceBase[ConsultaInDB, ConsultaCreate, ConsultaUpdate]):
    def __init__(self):
        super().__init__(consulta_repo)
    
    def create(self, db: Session, obj_in: ConsultaCreate) -> ConsultaInDB:
        # Verificar que la cita existe y está en estado adecuado
        cita = cita_repo.get(db, id=obj_in.cita_id)
        if not cita:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="La cita no existe"
            )
        
        # Asignar fecha actual si no se proporciona
        if not obj_in.fecha_consulta:
            obj_in.fecha_consulta = datetime.now()
        
        # Establecer versión inicial
        obj_in.version = "1.0"
        
        return super().create(db, obj_in=obj_in)
    
    def update(self, db: Session, id: int, obj_in: ConsultaUpdate) -> ConsultaInDB:
        consulta = self.get(db, id=id)
        
        # Incrementar versión al actualizar
        if consulta.version:
            version_parts = consulta.version.split('.')
            version_parts[-1] = str(int(version_parts[-1]) + 1)
            obj_in.version = '.'.join(version_parts)
        
        return super().update(db, id=id, obj_in=obj_in)
    
    def get_by_cita(self, db: Session, cita_id: int) -> ConsultaInDB:
        consulta = consulta_repo.get_by_cita(db, cita_id=cita_id)
        if not consulta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No se encontró consulta para esta cita"
            )
        return consulta
    
    def get_by_colaborador(self, db: Session, colaborador_id: int) -> list[ConsultaInDB]:
        return consulta_repo.get_by_colaborador(db, colaborador_id=colaborador_id)

consulta_service = ConsultaService()