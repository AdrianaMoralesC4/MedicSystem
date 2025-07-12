def test_create_colaborador(client, test_admin_user):
    headers_admin = {"Authorization": f"Bearer {test_admin_user['access_token']}"}
    response = client.post(
        "/api/v1/colaboradores/",
        json={
            "usuario_id": test_admin_user["id"],
            "cedula": "0987654321",
            "especialidad": "Cardiología",
            "contacto": "0988888888"
        },
        headers=headers_admin
    )
    assert response.status_code == 201
    assert "Cardiología" in response.json()["especialidad"]
