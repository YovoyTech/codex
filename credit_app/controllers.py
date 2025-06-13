"""FastAPI controller for credit validation."""

from typing import Dict

try:
    from fastapi import APIRouter, FastAPI
    from pydantic import BaseModel
except ImportError:  # pragma: no cover
    APIRouter = None
    FastAPI = None
    BaseModel = object  # type: ignore

from .models import ClientData, ValidationResult
from .services import api_clients, decision_service, odoo_service, notification_service

if APIRouter:
    router = APIRouter()
else:
    router = None


class ClientRequest(BaseModel):
    name: str
    id_number: str
    address: str
    phone: str
    email: str


if router:

    @router.post("/validate")
    def validate_client(data: ClientRequest) -> Dict[str, str]:
        result = ValidationResult(
            ccss_status=api_clients.ccss_status(data.id_number),
            sugef_status=api_clients.sugef_status(data.id_number),
            bcr_history_good=api_clients.bcr_history(data.id_number),
            protectora_deuda=api_clients.protectora_deuda(data.id_number),
            hacienda_status=api_clients.hacienda_status(data.id_number),
        )
        decision = decision_service.decide(result)
        odoo = odoo_service.OdooClient()
        if decision.approved:
            odoo.create_lead({"name": data.name, "email_from": data.email})
            notification_service.send_email(
                data.email, "Aprobado", "Su tarjeta fue aprobada"
            )
            return {"status": "approved"}
        else:
            odoo.create_lead(
                {
                    "name": data.name,
                    "email_from": data.email,
                    "description": decision.reason,
                }
            )
            notification_service.send_email(
                data.email, "Rechazado", decision.reason or ""
            )
            return {"status": "rejected", "reason": decision.reason}


if FastAPI:
    app = FastAPI()
    if router:
        app.include_router(router)
else:
    app = None
