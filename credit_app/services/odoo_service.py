"""Service to interact with Odoo via odoorpc."""
from typing import Dict, Any
import os

try:
    import odoorpc
except ImportError:  # pragma: no cover - optional dependency
    odoorpc = None

class OdooClient:
    def __init__(self):
        if odoorpc:
            host = os.getenv("ODOO_HOST", "localhost")
            db = os.getenv("ODOO_DB", "test")
            user = os.getenv("ODOO_USER", "admin")
            password = os.getenv("ODOO_PASSWORD", "admin")
            self.odoo = odoorpc.ODOO(host)
            self.odoo.login(db, user, password)
        else:
            self.odoo = None

    def create_lead(self, data: Dict[str, Any]) -> None:
        if not self.odoo:
            return
        self.odoo.env["crm.lead"].create(data)
