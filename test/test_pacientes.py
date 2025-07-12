def test_create_paciente(client, test_user):
    headers_user = {"Authorization": f"Bearer {test_user['access_token']}"}
    
    # Ahora permitimos crear paciente si el usuario es admin o es el mismo usuario (es_paciente)
    response = client.post(
        "/api/v1/pacientes/",
        json={
            "usuario_id": test_user["id"],
            "nombres": "Paciente Test",
            "cedula": "1234567890",
            "contacto": "0999999999"
        },
        headers=headers_user
    )
    assert response.status_code == 201, f"Error creando paciente: {response.text}"


