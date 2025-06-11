# Credit Validation App

This module provides a simple FastAPI service to automate credit validation for customers requesting a card. It integrates with external services and Odoo.

## Usage

```bash
uvicorn credit_app.main:app --reload
```

POST `/apply` with the following JSON payload:

```json
{
  "nombre": "Carlos",
  "cedula": "10101010",
  "correo": "carlos@example.com",
  "telefono": "88888888",
  "direccion": "San José"
}
```

The response indicates whether the client was approved and, if applicable, the shipping tracking number.
