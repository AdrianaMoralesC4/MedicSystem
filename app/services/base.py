from typing import Generic, TypeVar, Any
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class ServiceBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, repository: Any):
        self.repository = repository
    
    def get(self, db: Session, id: int) -> ModelType:
        obj = self.repository.get(db, id=id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Objeto no encontrado"
            )
        return obj
    
    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return self.repository.get_multi(db, skip=skip, limit=limit)
    
    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        return self.repository.create(db, obj_in=obj_in)
    
    def update(self, db: Session, id: int, obj_in: UpdateSchemaType | dict[str, Any]) -> ModelType:
        obj = self.repository.get(db, id=id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Objeto no encontrado"
            )
        return self.repository.update(db, db_obj=obj, obj_in=obj_in)
    
    def remove(self, db: Session, id: int) -> ModelType:
        obj = self.repository.get(db, id=id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Objeto no encontrado"
            )
        return self.repository.remove(db, id=id)