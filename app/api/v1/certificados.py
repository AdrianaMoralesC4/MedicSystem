from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.certificado import CertificadoCreate, CertificadoInDB
from app.schemas.usuario import UsuarioInDB
from app.core.security import get_current_active_user
from app.services.certificado import certificado_service
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=CertificadoInDB, status_code=201)
def create_certificado(
    certificado: CertificadoCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_active_user)
):
    if not current_user.es_colaborador:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo colaboradores de salud pueden emitir certificados"
        )
    return certificado_service.create(db, obj_in=certificado)

@router.get("/{codigo_verificacion}", response_model=CertificadoInDB)
def read_certificado(
    codigo_verificacion: str,
    db: Session = Depends(get_db)
):
    return certificado_service.get_by_codigo(db, codigo=codigo_verificacion)
