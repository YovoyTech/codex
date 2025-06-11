"""Simulated API client for Protectora de Crédito"""
from typing import Dict

def get_active_debt(cedula: str) -> Dict[str, str]:
    """Return a fake debt report."""
    return {"deuda": "NINGUNA"}
