def test_create_certificado(client, test_user, test_admin_user):
    headers_user = {"Authorization": f"Bearer {test_user['access_token']}"}
    headers_admin = {"Authorization": f"Bearer {test_admin_user['access_token']}"}

    # Crear paciente (admin)
    paciente_response = client.post("/api/v1/pacientes/", json={
        "usuario_id": test_user["id"],
        "nombres": "Paciente Certificado",
        "cedula": "3333333333"
    }, headers=headers_admin)
    assert paciente_response.status_code == 201, f"Error creando paciente: {paciente_response.text}"
    paciente = paciente_response.json()

    # Crear colaborador (admin)
    colaborador_response = client.post("/api/v1/colaboradores/", json={
        "usuario_id": test_admin_user["id"],
        "cedula": "4444444444",
        "especialidad": "Medicina General"
    }, headers=headers_admin)
    assert colaborador_response.status_code == 201, f"Error creando colaborador: {colaborador_response.text}"
    colaborador = colaborador_response.json()

    # Crear cita (usuario normal)
    cita_response = client.post("/api/v1/citas/", json={
        "paciente_id": paciente["id"],
        "colaborador_id": colaborador["id"],
        "fecha_hora": "2025-07-21T11:00:00Z",
        "motivo": "Consulta general"
    }, headers=headers_user)
    assert cita_response.status_code == 201, f"Error creando cita: {cita_response.text}"
    cita = cita_response.json()

    # Crear consulta (admin)
    consulta_response = client.post("/api/v1/consultas/", json={
        "cita_id": cita["id"],
        "colaborador_id": colaborador["id"]
    }, headers=headers_admin)
    assert consulta_response.status_code == 201, f"Error creando consulta: {consulta_response.text}"
    consulta = consulta_response.json()

    # Crear certificado (admin) - sin enviar campos generados
    certificado_response = client.post("/api/v1/certificados/", json={
        "consulta_id": consulta["id"],
        "colaborador_id": colaborador["id"],
        "tipo_certificado": "REPOSO",
        "contenido": "Reposo por 3 días"
    }, headers=headers_admin)
    assert certificado_response.status_code == 201, f"Error creando certificado: {certificado_response.text}"
    certificado = certificado_response.json()
    assert certificado["tipo_certificado"] == "REPOSO"
    assert "codigo_verificacion" in certificado
    assert "fecha_emision" in certificado




