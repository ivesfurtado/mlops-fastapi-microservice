# src/core/server.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.v1.routes import router as prediction_router


app = FastAPI()

# Include the prediction router
app.include_router(prediction_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
