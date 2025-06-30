from sqlalchemy.orm import Session
from app.models.certificado import Certificado
from app.schemas.certificado import CertificadoCreate, CertificadoUpdate
from app.repositories.base import CRUDBase

class CRUDCertificado(CRUDBase[Certificado, CertificadoCreate, CertificadoUpdate]):
    def get_by_codigo(self, db: Session, codigo: str) -> Certificado | None:
        return db.query(Certificado).filter(Certificado.codigo_verificacion == codigo).first()
    
    def get_by_consulta(self, db: Session, consulta_id: int) -> list[Certificado]:
        return db.query(Certificado).filter(Certificado.consulta_id == consulta_id).all()

certificado_repo = CRUDCertificado(Certificado)