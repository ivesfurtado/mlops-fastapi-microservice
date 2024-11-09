# tests/test_api.py

from fastapi.testclient import TestClient
from src.core.server import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_predict():
    response = client.post(
        "/api/v1/predict",
        json={"features": {"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()
