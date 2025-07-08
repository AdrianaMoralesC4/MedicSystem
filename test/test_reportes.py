def test_generate_reporte_medico(client, test_user):
    response = client.post(
        "/api/v1/reportes/medicos",
        json={"filtros": {"fecha_inicio": "2025-01-01", "especialidad": "Cardiología"}},
        headers={"Authorization": f"Bearer {test_user['access_token']}"}
    )
    assert response.status_code == 201
    assert response.json()["tipo_reporte"] == "MEDICO"