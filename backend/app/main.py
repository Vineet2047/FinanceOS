from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.init_db import create_database
from app.api.account_router import router as account_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()

    yield

app = FastAPI(
    title="FinanceOS API",
    version="0.1.0",
    lifespan=lifespan,
)

@app.get("/")
async def root():
    return {
        "application": "FinanceOS",
        "status": "Running",
        "version": "0.1.0",
    }

app.include_router(account_router)
