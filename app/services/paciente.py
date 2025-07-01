from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.paciente import PacienteCreate, PacienteUpdate, PacienteInDB
from app.repositories.paciente import paciente_repo
from app.services.base import ServiceBase

class PacienteService(ServiceBase[PacienteInDB, PacienteCreate, PacienteUpdate]):
    def __init__(self):
        super().__init__(paciente_repo)
    
    def create(self, db: Session, obj_in: PacienteCreate) -> PacienteInDB:
        if paciente_repo.get_by_cedula(db, cedula=obj_in.cedula):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un paciente con esta cédula",
            )
        return super().create(db, obj_in=obj_in)

paciente_service = PacienteService()