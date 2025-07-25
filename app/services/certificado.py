from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.schemas.certificado import CertificadoCreate, CertificadoUpdate, CertificadoInDB
from app.repositories.certificado import certificado_repo
from app.services.base import ServiceBase
from app.utils.helpers import generate_verification_code

class CertificadoService(ServiceBase[CertificadoInDB, CertificadoCreate, CertificadoUpdate]):
    def __init__(self):
        super().__init__(certificado_repo)
    
    def create(self, db: Session, obj_in: CertificadoCreate) -> CertificadoInDB:
        # Generar código de verificación único
        codigo = generate_verification_code()
        while certificado_repo.get_by_codigo(db, codigo=codigo):
            codigo = generate_verification_code()
        
        # Generar fecha de emisión en UTC
        fecha_emision = datetime.now(timezone.utc)

        # Preparar datos para guardar
        data = obj_in.model_dump()
        data["codigo_verificacion"] = codigo
        data["fecha_emision"] = fecha_emision
        obj_in_with_generated = CertificadoCreate(**data)

        return super().create(db, obj_in=obj_in_with_generated)
    
    def get_by_codigo(self, db: Session, codigo: str) -> CertificadoInDB:
        certificado = certificado_repo.get_by_codigo(db, codigo=codigo)
        if not certificado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Certificado no encontrado"
            )
        return certificado
    
    def get_by_consulta(self, db: Session, consulta_id: int) -> list[CertificadoInDB]:
        return certificado_repo.get_by_consulta(db, consulta_id=consulta_id)

certificado_service = CertificadoService()

