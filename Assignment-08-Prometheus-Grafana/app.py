"""Reconstructed runnable Iris API consistent with the documented metrics.
Not a byte-for-byte copy of the original local Assignment 8 source.
"""
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from prometheus_client import Counter, make_asgi_app
from sklearn.datasets import load_iris
import joblib

app = FastAPI(title="Iris Monitoring API")
app.mount("/metrics", make_asgi_app())

PREDICTIONS = Counter("iris_predictions_total", "Predictions by species", ["species"])
HTTP_REQUESTS = Counter("iris_http_requests_total", "HTTP requests by endpoint", ["endpoint"])
SPECIES = list(load_iris().target_names)
MODEL_PATH = Path(__file__).parent / "iris_model.joblib"

class IrisInput(BaseModel):
    features: list[float] = Field(min_length=4, max_length=4)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: IrisInput):
    HTTP_REQUESTS.labels(endpoint="/predict").inc()
    if not MODEL_PATH.exists():
        raise HTTPException(status_code=503, detail="Run train_model.py first")
    model = joblib.load(MODEL_PATH)
    index = int(model.predict([payload.features])[0])
    species = SPECIES[index]
    PREDICTIONS.labels(species=species).inc()
    return {"prediction": index, "species": species}
