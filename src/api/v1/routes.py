# src/api/v1/routes.py

from fastapi import APIRouter, Depends
from src.app.services.model_service import PredictionInput, PredictionService

router = APIRouter()

@router.post("/predict")
async def predict(input_data: PredictionInput, service: PredictionService = Depends()):
    prediction = service.predict(input_data)
    return {"prediction": prediction.tolist()}
