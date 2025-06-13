import pytest

fastapi = pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from credit_app.controllers import app


def test_validate_route_exists():
    client = TestClient(app)
    response = client.post(
        "/validate",
        json={
            "name": "John Doe",
            "id_number": "123",
            "address": "Nowhere",
            "phone": "1234",
            "email": "j@example.com",
        },
    )
    assert response.status_code == 200
    assert "status" in response.json()
