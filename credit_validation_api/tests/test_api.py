from fastapi.testclient import TestClient
from credit_validation_api.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_apply_approved(monkeypatch):
    def mock_run_all_checks(id_number):
        return {"ccss": True, "sugef": True, "bcr": True, "protectora": True, "hacienda": True}
    monkeypatch.setattr("credit_validation_api.services.external_apis.run_all_checks", mock_run_all_checks)
    resp = client.post("/apply", json={
        "name": "John Doe",
        "id_number": "1234",
        "address": "Addr",
        "phone": "555",
        "email": "john@example.com"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["approved"] is True
    assert data["card_type"] == "virtual"


def test_apply_rejected(monkeypatch):
    def mock_run_all_checks(id_number):
        return {"ccss": False, "sugef": True, "bcr": True, "protectora": True, "hacienda": True}
    monkeypatch.setattr("credit_validation_api.services.external_apis.run_all_checks", mock_run_all_checks)
    resp = client.post("/apply", json={
        "name": "Jane Doe",
        "id_number": "4321",
        "address": "Addr",
        "phone": "555",
        "email": "jane@example.com"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["approved"] is False
    assert data["card_type"] is None
