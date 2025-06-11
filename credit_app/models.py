from pydantic import BaseModel, Field
from typing import Optional

class ClientApplication(BaseModel):
    nombre: str
    cedula: str
    direccion: str
    telefono: str
    correo: str
    virtual: bool = Field(False, description="True if the card is virtual")

class ValidationResult(BaseModel):
    aprobado: bool
    mensaje: str
    tarjeta_virtual: Optional[bool] = None
