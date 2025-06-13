# Credit Validation App

This module implements a basic credit validation flow using FastAPI. It queries
external services and registers results in Odoo. The endpoints are defined under
`credit_app.controllers` and the application object is available as
`credit_app.main.app`.

Unit tests covering the decision logic and the API route can be run with:

```bash
pytest credit_app/tests
```
