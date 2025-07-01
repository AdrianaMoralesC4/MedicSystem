from datetime import datetime, timedelta
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.cita import CitaCreate, CitaUpdate, CitaInDB
from app.repositories.cita import cita_repo
from app.services.base import ServiceBase
from ..utils.enums import EstadoCita

class CitaService(ServiceBase[CitaInDB, CitaCreate, CitaUpdate]):
    def __init__(self):
        super().__init__(cita_repo)
    
    def create(self, db: Session, obj_in: CitaCreate) -> CitaInDB:
        # Verificar disponibilidad del colaborador
        citas_existentes = cita_repo.get_by_colaborador(db, colaborador_id=obj_in.colaborador_id)
        for cita in citas_existentes:
            if abs((cita.fecha_hora - obj_in.fecha_hora).total_seconds()) < 1800:  # 30 minutos
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El colaborador ya tiene una cita en ese horario",
                )
        
        return super().create(db, obj_in=obj_in)
    
    def cancelar_cita(self, db: Session, id: int) -> CitaInDB:
        cita = self.get(db, id=id)
        if cita.estado != EstadoCita.SOLICITADA:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Solo se pueden cancelar citas en estado SOLICITADA",
            )
        
        cita.estado = EstadoCita.CANCELADA
        db.add(cita)
        db.commit()
        db.refresh(cita)
        return cita
    
    def confirmar_cita(self, db: Session, id: int) -> CitaInDB:
        cita = self.get(db, id=id)
        if cita.estado != EstadoCita.SOLICITADA:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Solo se pueden confirmar citas en estado SOLICITADA",
            )
        
        cita.estado = EstadoCita.CON

cita_service = CitaService()