def test_create_paciente(client, test_user):
    response = client.post(
        "/api/v1/pacientes/",
        json={
            "usuario_id": test_user["id"],
            "nombres": "Paciente Test",
            "cedula": "1234567890",
            "contacto": "0999999999"
        },
        headers={"Authorization": f"Bearer {test_user['access_token']}"}
    )
    assert response.status_code == 201
    assert response.json()["cedula"] == "1234567890"