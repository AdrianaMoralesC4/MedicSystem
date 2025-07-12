import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db
from app.repositories.usuario import usuario_repo

# Configuración de base de datos de prueba SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_db():
    # Crear tablas
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(test_db):
    # Override get_db para usar la base de datos de prueba
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

@pytest.fixture(scope="module")
def test_user(client, test_db):
    user_data = {
        "nombre_usuario": "testuser",
        "correo_electronico": "testuser@example.com",
        "contrasena": "testpass",
        "es_administrador": False,
        "es_paciente": True,
        "es_colaborador": False
    }
    # Registro usuario normal
    response = client.post("/api/v1/usuarios/registro", json=user_data)
    assert response.status_code == 201

    # Obtener usuario de DB para acceder a atributos
    db_user = usuario_repo.get_by_username(test_db, username=user_data["nombre_usuario"])
    db_user.es_paciente = True
    test_db.commit()

    # Login para obtener token
    login_response = client.post(
        "/api/v1/usuarios/login",
        data={"username": user_data["nombre_usuario"], "password": user_data["contrasena"]},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert login_response.status_code == 200

    return {
        **response.json(),
        "id": db_user.id,
        "access_token": login_response.json()["access_token"]
    }

@pytest.fixture(scope="module")
def test_admin_user(client, test_db):
    admin_data = {
        "nombre_usuario": "adminuser",
        "correo_electronico": "admin@example.com",
        "contrasena": "adminpass",
        "es_administrador": True,
        "es_paciente": False,
        "es_colaborador": True  # ✅ Ahora también colaborador
    }
    # Registro admin
    response = client.post("/api/v1/usuarios/registro", json=admin_data)
    assert response.status_code == 201

    # Convertir en admin y colaborador en la DB
    db_user = usuario_repo.get_by_username(test_db, username=admin_data["nombre_usuario"])
    db_user.es_administrador = True
    db_user.es_colaborador = True
    test_db.commit()

    # Login admin para token
    login_response = client.post(
        "/api/v1/usuarios/login",
        data={"username": admin_data["nombre_usuario"], "password": admin_data["contrasena"]},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert login_response.status_code == 200

    return {
        **response.json(),
        "id": db_user.id,
        "access_token": login_response.json()["access_token"]
    }
