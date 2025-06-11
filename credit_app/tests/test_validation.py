from credit_app.models import ApplicationRequest
from credit_app.services.validation import CreditValidator


def test_approved():
    validator = CreditValidator()
    req = ApplicationRequest(
        nombre="Test", cedula="1", direccion="X", telefono="123", correo="a@b.c"
    )
    resp = validator.process_application(req)
    assert resp.aprobado is True
    assert resp.numero_rastreo == "TRACK123"


def test_rejected(monkeypatch):
    validator = CreditValidator()

    def fake_ccss(cedula: str):
        return {"asegurado": False}

    monkeypatch.setattr(
        "credit_app.services.validation.consulta_ccss", fake_ccss
    )

    req = ApplicationRequest(
        nombre="Test", cedula="1", direccion="X", telefono="123", correo="a@b.c"
    )
    resp = validator.process_application(req)
    assert resp.aprobado is False
    assert resp.numero_rastreo is None
