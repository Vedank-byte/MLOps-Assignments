"""Representative tests reconstructed from report; not copied from original test file."""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    assert client.get("/").status_code == 200

def test_health():
    assert client.get("/health").json()["status"] == "ok"

def test_model_info():
    assert client.get("/model-info").status_code == 200

def test_negative_measurement_rejected():
    payload = {"sepal_length": -1, "sepal_width": 3.5,
               "petal_length": 1.4, "petal_width": 0.2}
    assert client.post("/predict", json=payload).status_code == 422

def test_setosa_prediction():
    payload = {"sepal_length": 5.1, "sepal_width": 3.5,
               "petal_length": 1.4, "petal_width": 0.2}
    assert client.post("/predict", json=payload).json()["species"] == "setosa"
