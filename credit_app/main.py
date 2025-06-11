from fastapi import FastAPI
from .models import ApplicationRequest, ApplicationResponse
from .services.validation import CreditValidator

app = FastAPI()
validator = CreditValidator()


@app.get("/ping")
def ping() -> dict:
    return {"status": "ok"}


@app.post("/apply", response_model=ApplicationResponse)
def apply(data: ApplicationRequest):
    return validator.process_application(data)
