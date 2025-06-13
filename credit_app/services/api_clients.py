"""API client implementations for external services.
These use the `requests` library but can fall back to stubs if the module isn't
available in the environment.
"""

from typing import Any, Dict

try:
    import requests  # type: ignore
except ImportError:  # pragma: no cover
    requests = None  # type: ignore

BASE_URL = "https://api.example.com"


def _get(endpoint: str) -> Dict[str, Any]:
    if requests is None:
        # Stubbed response when requests is unavailable
        return {"status": "unavailable"}
    resp = requests.get(f"{BASE_URL}/{endpoint}", timeout=5)
    resp.raise_for_status()
    return resp.json()


def ccss_status(id_number: str) -> bool:
    data = _get(f"ccss/{id_number}")
    return data.get("insured", False)


def sugef_status(id_number: str) -> bool:
    data = _get(f"sugef/{id_number}")
    return data.get("credit_ok", False)


def bcr_history(id_number: str) -> bool:
    data = _get(f"bcr/{id_number}")
    return data.get("good_history", False)


def protectora_deuda(id_number: str) -> bool:
    data = _get(f"protectora/{id_number}")
    return not data.get("active_debt", False)


def hacienda_status(id_number: str) -> bool:
    data = _get(f"hacienda/{id_number}")
    return data.get("compliant", False)
