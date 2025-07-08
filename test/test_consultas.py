def test_create_consulta(client, test_user):
    # Crear cita primero
    cita = client.post("/api/v1/citas/", json={
        "paciente_id": 1,
        "colaborador_id": 1,
        "fecha_hora": "2025-07-20T10:00:00"
    }).json()

    response = client.post(
        "/api/v1/consultas/",
        json={
            "cita_id": cita["id"],
            "colaborador_id": 1,
            "diagnostico": "Resfriado común"
        },
        headers={"Authorization": f"Bearer {test_user['access_token']}"}
    )
    assert response.status_code == 201
    assert "Resfriado" in response.json()["diagnostico"]