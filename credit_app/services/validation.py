from .apis import (
    consulta_ccss,
    consulta_sugef,
    consulta_bcr,
    consulta_protectora,
    consulta_hacienda,
)
from .mimoto_client import MimotoClient
from .odoo_client import OdooClient
from .notifier import Notifier
from ..models import ApplicationRequest, ApplicationResponse


class CreditValidator:
    def __init__(self) -> None:
        self.mimoto = MimotoClient()
        self.odoo = OdooClient()
        self.notifier = Notifier()

    def process_application(self, req: ApplicationRequest) -> ApplicationResponse:
        ccss = consulta_ccss(req.cedula)
        sugef = consulta_sugef(req.cedula)
        bcr = consulta_bcr(req.cedula)
        protectora = consulta_protectora(req.cedula)
        hacienda = consulta_hacienda(req.cedula)

        if all(
            [
                ccss.get("asegurado"),
                sugef.get("score") == "A",
                bcr.get("historial") == "limpio",
                not protectora.get("deuda"),
                hacienda.get("al_dia"),
            ]
        ):
            track = self.mimoto.create_order(req.direccion)
            self.odoo.record_application(req.__dict__, True)
            self.notifier.notify_approval(req.correo, "Su solicitud fue aprobada")
            return ApplicationResponse(
                aprobado=True, mensaje="Aprobado", numero_rastreo=track
            )

        reason = "No cumple con los criterios"
        self.odoo.record_application(req.__dict__, False)
        self.notifier.notify_rejection(req.correo, reason)
        return ApplicationResponse(aprobado=False, mensaje=reason)
