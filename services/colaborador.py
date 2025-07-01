from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.colaborador import ColaboradorCreate, ColaboradorUpdate, ColaboradorInDB
from app.repositories.colaborador import colaborador_repo
from app.services.base import ServiceBase

class ColaboradorService(ServiceBase[ColaboradorInDB, ColaboradorCreate, ColaboradorUpdate]):
    def __init__(self):
        super().__init__(colaborador_repo)
    
    def create(self, db: Session, obj_in: ColaboradorCreate) -> ColaboradorInDB:
        if colaborador_repo.get_by_cedula(db, cedula=obj_in.cedula):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un colaborador con esta cédula",
            )
        return super().create(db, obj_in=obj_in)
    
    def get_by_especialidad(self, db: Session, especialidad: str) -> list[ColaboradorInDB]:
        return colaborador_repo.get_by_especialidad(db, especialidad=especialidad)

colaborador_service = ColaboradorService()