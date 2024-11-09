# tests/test_services.py

from src.app.services.model_service import PredictionService, PredictionInput

def test_prediction_service():
    service = PredictionService()

    input_data = PredictionInput(features={"sepal length (cm)": 5.1,
                                           "sepal width (cm)": 3.5,
                                           "petal length (cm)": 1.4,
                                           "petal width (cm)": 0.2})

    prediction = service.predict(input_data)

    assert len(prediction) == 1  # Ensure one prediction is returned.
