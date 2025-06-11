"""Simulated external API calls."""

from typing import Dict


def check_ccss(id_number: str) -> bool:
    # Placeholder for CCSS API call
    return True


def check_sugef(id_number: str) -> bool:
    # Placeholder for SUGEF API call
    return True


def check_bcr(id_number: str) -> bool:
    # Placeholder for Banco de Costa Rica API call
    return True


def check_protectora(id_number: str) -> bool:
    # Placeholder for Protectora de Crédito API call
    return True


def check_hacienda(id_number: str) -> bool:
    # Placeholder for Ministerio de Hacienda API call
    return True


def run_all_checks(id_number: str) -> Dict[str, bool]:
    return {
        "ccss": check_ccss(id_number),
        "sugef": check_sugef(id_number),
        "bcr": check_bcr(id_number),
        "protectora": check_protectora(id_number),
        "hacienda": check_hacienda(id_number),
    }
