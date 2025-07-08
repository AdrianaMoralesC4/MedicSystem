from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioInDB, UsuarioLogin
from app.core.security import get_current_admin_user, create_access_token
from app.services.usuario import usuario_service
from app.core.database import get_db

router = APIRouter()

# Endpoint público para registro
@router.post("/registro", response_model=UsuarioInDB, status_code=201)
async def register_user(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return usuario_service.create(db, obj_in=usuario)

# Endpoint público para login
@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = usuario_service.authenticate(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    access_token = create_access_token(data={"sub": user.nombre_usuario})
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoints protegidos (solo admin)
@router.post("/", response_model=UsuarioInDB)
async def create_user_admin(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_admin_user)
):
    return usuario_service.create(db, obj_in=usuario)

@router.get("/{user_id}", response_model=UsuarioInDB)
async def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UsuarioInDB = Depends(get_current_admin_user)
):
    return usuario_service.get(db, id=user_id)