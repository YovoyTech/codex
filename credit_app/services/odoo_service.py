"""Odoo integration helpers."""

from typing import Any, Dict

try:
    import odoorpc  # type: ignore
except ImportError:  # pragma: no cover
    odoorpc = None  # type: ignore


class OdooClient:
    def __init__(
        self,
        host: str = "localhost",
        db: str = "odoo",
        user: str = "admin",
        password: str = "admin",
    ):
        if odoorpc is None:
            self.conn = None
        else:
            self.conn = odoorpc.ODOO(host, port=8069)
            self.conn.login(db, user, password)

    def create_lead(self, values: Dict[str, Any]) -> Any:
        if self.conn is None:
            return None
        return self.conn.env["crm.lead"].create(values)
