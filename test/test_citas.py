def test_create_cita(client, test_user):
    # Primero crear paciente y colaborador
    paciente = client.post("/api/v1/pacientes/", json={
        "usuario_id": test_user["id"],
        "nombres": "Paciente Cita",
        "cedula": "1111111111"
    }).json()
    
    colaborador = client.post("/api/v1/colaboradores/", json={
        "usuario_id": test_user["id"],
        "cedula": "2222222222",
        "especialidad": "Pediatría"
    }).json()

    response = client.post(
        "/api/v1/citas/",
        json={
            "paciente_id": paciente["id"],
            "colaborador_id": colaborador["id"],
            "fecha_hora": "2025-07-20T10:00:00",
            "motivo": "Control rutinario"
        },
        headers={"Authorization": f"Bearer {test_user['access_token']}"}
    )
    assert response.status_code == 201
    assert response.json()["estado"] == "SOLICITADA"