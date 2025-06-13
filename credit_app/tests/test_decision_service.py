from credit_app.services.decision_service import decide
from credit_app.models import ValidationResult


def test_decision_approved():
    result = ValidationResult(True, True, True, True, True)
    decision = decide(result)
    assert decision.approved


def test_decision_rejected():
    result = ValidationResult(True, False, True, True, True)
    decision = decide(result)
    assert not decision.approved
    assert decision.reason
