def test_create_certificado(client, test_user):
    consulta = client.post("/api/v1/consultas/", json={
        "cita_id": 1,
        "colaborador_id": 1
    }).json()

    response = client.post(
        "/api/v1/certificados/",
        json={
            "consulta_id": consulta["id"],
            "colaborador_id": 1,
            "tipo_certificado": "REPOSO",
            "contenido": "Reposo por 3 días"
        },
        headers={"Authorization": f"Bearer {test_user['access_token']}"}
    )
    assert response.status_code == 201
    assert len(response.json()["codigo_verificacion"]) == 16