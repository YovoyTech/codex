"""Simulated API client for SUGEF"""
from typing import Dict

def get_credit_condition(cedula: str) -> Dict[str, str]:
    """Return a fake credit condition."""
    return {"condicion": "NORMAL"}
