# src/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/model.pkl")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
