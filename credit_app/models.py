from dataclasses import dataclass
from typing import Optional


@dataclass
class ClientData:
    name: str
    id_number: str
    address: str
    phone: str
    email: str


@dataclass
class ValidationResult:
    ccss_status: bool
    sugef_status: bool
    bcr_history_good: bool
    protectora_deuda: bool
    hacienda_status: bool


@dataclass
class Decision:
    approved: bool
    reason: Optional[str] = None
