def test_create_consulta(client, test_user, test_admin_user):
    headers_user = {"Authorization": f"Bearer {test_user['access_token']}"}
    headers_admin = {"Authorization": f"Bearer {test_admin_user['access_token']}"}

    # Crear paciente (usuario normal)
    paciente_response = client.post("/api/v1/pacientes/", json={
        "usuario_id": test_user["id"],
        "nombres": "Paciente Consulta",
        "cedula": "5555555555"
    }, headers=headers_user)
    assert paciente_response.status_code == 201, f"Error creando paciente: {paciente_response.text}"
    paciente = paciente_response.json()

    # Crear colaborador (admin)
    colaborador_response = client.post("/api/v1/colaboradores/", json={
        "usuario_id": test_admin_user["id"],
        "cedula": "6666666666",
        "especialidad": "Medicina Interna"
    }, headers=headers_admin)
    assert colaborador_response.status_code == 201, f"Error creando colaborador: {colaborador_response.text}"
    colaborador = colaborador_response.json()

    # Crear cita (usuario normal)
    cita_response = client.post("/api/v1/citas/", json={
        "paciente_id": paciente["id"],
        "colaborador_id": colaborador["id"],
        "fecha_hora": "2025-07-20T10:00:00",
        "motivo": "Revisión general"
    }, headers=headers_user)
    assert cita_response.status_code == 201, f"Error creando cita: {cita_response.text}"
    cita = cita_response.json()

    # Crear consulta (admin)
    consulta_response = client.post("/api/v1/consultas/", json={
        "cita_id": cita["id"],
        "colaborador_id": colaborador["id"],
        "diagnostico": "Resfriado común"
    }, headers=headers_admin)
    assert consulta_response.status_code == 201, f"Error creando consulta: {consulta_response.text}"
    consulta = consulta_response.json()

    assert "Resfriado" in consulta["diagnostico"]

