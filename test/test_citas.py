def test_create_cita(client, test_user, test_admin_user):
    headers_user = {"Authorization": f"Bearer {test_user['access_token']}"}
    headers_admin = {"Authorization": f"Bearer {test_admin_user['access_token']}"}

    # Crear paciente (usuario normal)
    paciente_response = client.post("/api/v1/pacientes/", json={
        "usuario_id": test_user["id"],
        "nombres": "Paciente Cita",
        "cedula": "1111111111"
    }, headers=headers_user)
    assert paciente_response.status_code == 201, f"Error creando paciente: {paciente_response.text}"
    paciente = paciente_response.json()

    # Crear colaborador (admin)
    colaborador_response = client.post("/api/v1/colaboradores/", json={
        "usuario_id": test_admin_user["id"],
        "cedula": "2222222222",
        "especialidad": "Pediatría"
    }, headers=headers_admin)
    assert colaborador_response.status_code == 201, f"Error creando colaborador: {colaborador_response.text}"
    colaborador = colaborador_response.json()

    # Crear cita (usuario normal)
    cita_response = client.post("/api/v1/citas/", json={
        "paciente_id": paciente["id"],
        "colaborador_id": colaborador["id"],
        "fecha_hora": "2025-07-20T10:00:00",
        "motivo": "Control rutinario"
    }, headers=headers_user)
    assert cita_response.status_code == 201, f"Error creando cita: {cita_response.text}"

    cita = cita_response.json()
    assert cita["estado"] == "SOLICITADA"
