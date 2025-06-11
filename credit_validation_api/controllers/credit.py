from fastapi import APIRouter
from ..models import ClientApplication, ApplicationResult
from ..services import external_apis, odoo_service, notification_service, card_service

router = APIRouter()


def evaluate_application(data: ClientApplication) -> ApplicationResult:
    checks = external_apis.run_all_checks(data.id_number)
    approved = all(checks.values())
    if approved:
        card_type = card_service.generate_card()
        card_service.create_shipping_order(card_type)
        odoo_service.register_client(data.dict())
        notification_service.notify_client(
            data.email,
            f"Su tarjeta {card_type} ha sido aprobada."
        )
        message = "Aprobado"
    else:
        card_type = None
        message = "Rechazado por validaciones negativas"
    odoo_service.log_attempt(data.dict(), approved)
    return ApplicationResult(approved=approved, message=message, card_type=card_type)


@router.post("/apply", response_model=ApplicationResult)
async def apply(application: ClientApplication):
    return evaluate_application(application)


@router.get("/ping")
async def ping():
    return {"status": "ok"}
