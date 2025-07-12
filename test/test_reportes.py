from datetime import datetime, timedelta, timezone

def test_generate_reporte_medico(client, test_admin_user):
    headers_admin = {"Authorization": f"Bearer {test_admin_user['access_token']}"}
    future_date = (datetime.now(timezone.utc) + timedelta(days=1)).strftime("%Y-%m-%d")

    response = client.post(
        "/api/v1/reportes/medicos",
        json={"filtros": {"fecha_inicio": future_date, "especialidad": "Cardiología"}},
        headers=headers_admin
    )
    assert response.status_code == 201, f"Error generando reporte médico: {response.text}"
    reporte = response.json()
    assert reporte["tipo_reporte"] == "MEDICO"
    assert "fecha_creacion" in reporte

