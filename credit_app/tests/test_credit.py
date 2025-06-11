from fastapi.testclient import TestClient
from credit_app.main import app

client = TestClient(app)

def test_ping():
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_apply_success():
    payload = {
        "nombre": "Juan Perez",
        "cedula": "123",
        "direccion": "San Jose",
        "telefono": "5555",
        "correo": "juan@example.com",
        "virtual": True,
    }
    resp = client.post("/apply", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["aprobado"] is True
    assert data["mensaje"] == "Aprobado"
