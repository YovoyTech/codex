from fastapi import FastAPI
from .routers import credit

app = FastAPI(title="Credit Validation API")
app.include_router(credit.router)


@app.get("/ping")
def ping():
    return {"status": "ok"}

