from fastapi import FastAPI
from .controllers.credit import router as credit_router

app = FastAPI(title="Credit Validation API")
app.include_router(credit_router)
