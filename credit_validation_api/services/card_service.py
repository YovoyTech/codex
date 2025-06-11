"""Simulated card generation and shipping."""

from typing import Literal


def generate_card(virtual: bool = True) -> str:
    return "virtual" if virtual else "physical"


def create_shipping_order(card_type: str) -> None:
    # Placeholder for mimoto.express API call
    pass
