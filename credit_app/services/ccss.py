"""Simulated API client for CCSS"""
from typing import Dict

def check_status(cedula: str) -> Dict[str, str]:
    """Return a fake insurance status."""
    # Simulate API call
    return {"status": "ASEGURADO"}
