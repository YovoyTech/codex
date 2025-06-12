from fastapi import APIRouter
from ..models import ClientApplication, ValidationResult
from ..services import (
    ccss,
    sugef,
    bcr,
    protectora,
    hacienda,
    odoo_service,
    notification,
    shipping,
)

router = APIRouter()

odoo_client = odoo_service.OdooClient()


def evaluate(app: ClientApplication) -> ValidationResult:
    """Evaluate the responses from all services and approve or deny."""
    ccss_status = ccss.check_status(app.cedula)
    sugef_cond = sugef.get_credit_condition(app.cedula)
    bcr_hist = bcr.get_financial_history(app.cedula)
    debt = protectora.get_active_debt(app.cedula)
    tax = hacienda.get_tax_status(app.cedula)

    approved = all(
        (
            ccss_status.get("status") == "ASEGURADO",
            sugef_cond.get("condicion") == "NORMAL",
            bcr_hist.get("historial") == "LIMPIO",
            debt.get("deuda") == "NINGUNA",
            tax.get("situacion") == "AL DIA",
        )
    )

    if approved:
        tracking = shipping.create_order(app.direccion, app.nombre)
        odoo_client.create_lead(app.dict())
        notification.send_email(
            app.correo,
            "Solicitud aprobada",
            f"Su tarjeta sera enviada. Tracking: {tracking['tracking_id']}",
        )
        return ValidationResult(aprobado=True, mensaje="Aprobado", tarjeta_virtual=app.virtual)

    else:
        odoo_client.create_lead({**app.dict(), "status": "rejected"})
        notification.send_email(
            app.correo,
            "Solicitud rechazada",
            "No cumple con los criterios de aprobacion",
        )
        return ValidationResult(aprobado=False, mensaje="Rechazado")


@router.post("/apply", response_model=ValidationResult)
def apply_for_card(app: ClientApplication):
    return evaluate(app)
