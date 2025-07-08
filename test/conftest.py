import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db

# Configuración de base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(test_db):
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

@pytest.fixture(scope="module")
async def test_user(client):
    # Registro de usuario de prueba
    user_data = {
        "nombre_usuario": "testuser",
        "correo_electronico": "test@example.com",
        "contrasena": "testpass"
    }
    response = client.post("/api/v1/usuarios/registro", json=user_data)
    assert response.status_code == 201
    
    # Login para obtener token
    login_data = {
        "username": user_data["nombre_usuario"],
        "password": user_data["contrasena"]
    }
    login_response = client.post(
        "/api/v1/usuarios/login",
        data=login_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert login_response.status_code == 200
    
    return {
        **response.json(),
        "access_token": login_response.json()["access_token"]
    }