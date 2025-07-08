def test_create_user(client):
    response = client.post(
        "/api/v1/usuarios/",
        json={
            "nombre_usuario": "newuser",
            "correo_electronico": "user@example.com",
            "contrasena": "securepassword"
        }
    )
    assert response.status_code == 201
    assert "id" in response.json()

def test_login_user(client, test_user):
    response = client.post(
        "/api/v1/usuarios/login",
        data={
            "username": "testuser",
            "password": "testpass"
        }
    )
    assert response.status_code == 200
    assert "access_token" in response.json()