from pydantic import BaseModel
from typing import Optional

class ClientApplication(BaseModel):
    name: str
    id_number: str
    address: str
    phone: str
    email: str

class ApplicationResult(BaseModel):
    approved: bool
    message: str
    card_type: Optional[str] = None
