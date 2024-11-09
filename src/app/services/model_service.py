# src/app/services/model_service.py

import joblib
import pandas as pd
from pydantic import BaseModel
from src.core.config import settings

class PredictionInput(BaseModel):
    features: dict

class PredictionService:
    def __init__(self):
        self.model = joblib.load(settings.MODEL_PATH)

    def predict(self, input_data: PredictionInput):
        df = pd.DataFrame([input_data.features])
        return self.model.predict(df)
