def test_create_colaborador(client, test_user):
    response = client.post(
        "/api/v1/colaboradores/",
        json={
            "usuario_id": test_user["id"],
            "cedula": "0987654321",
            "especialidad": "Cardiología",
            "contacto": "0988888888"
        },
        headers={"Authorization": f"Bearer {test_user['access_token']}"}
    )
    assert response.status_code == 201
    assert "Cardiología" in response.json()["especialidad"]