from dataclasses import dataclass
from typing import Optional


@dataclass
class ApplicationRequest:
    nombre: str
    cedula: str
    direccion: str
    telefono: str
    correo: str


@dataclass
class ApplicationResponse:
    aprobado: bool
    mensaje: str
    numero_rastreo: Optional[str] = None
