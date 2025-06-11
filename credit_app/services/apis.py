"""Stub implementations of external API calls."""

from typing import Dict


def consulta_ccss(cedula: str) -> Dict[str, bool]:
    """Return asegurado status."""
    return {"asegurado": True}


def consulta_sugef(cedula: str) -> Dict[str, str]:
    """Return credit status."""
    return {"score": "A"}


def consulta_bcr(cedula: str) -> Dict[str, str]:
    """Return financial history."""
    return {"historial": "limpio"}


def consulta_protectora(cedula: str) -> Dict[str, bool]:
    """Return active debt flag."""
    return {"deuda": False}


def consulta_hacienda(cedula: str) -> Dict[str, bool]:
    """Return fiscal status."""
    return {"al_dia": True}
