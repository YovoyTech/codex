"""Decision logic for credit validation."""

from ..models import ValidationResult, Decision


def decide(result: ValidationResult) -> Decision:
    if all(
        [
            result.ccss_status,
            result.sugef_status,
            result.bcr_history_good,
            result.protectora_deuda,
            result.hacienda_status,
        ]
    ):
        return Decision(approved=True)
    reason = "Some checks failed"
    return Decision(approved=False, reason=reason)
