"""Simulated API client for Banco de Costa Rica"""
from typing import Dict

def get_financial_history(cedula: str) -> Dict[str, str]:
    """Return a fake financial history."""
    return {"historial": "LIMPIO"}
