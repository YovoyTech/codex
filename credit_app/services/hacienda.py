"""Simulated API client for Ministerio de Hacienda"""
from typing import Dict

def get_tax_status(cedula: str) -> Dict[str, str]:
    """Return a fake tax status."""
    return {"situacion": "AL DIA"}
