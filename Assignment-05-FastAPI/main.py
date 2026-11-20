"""Reconstructed API based on documented Assignment 5 endpoints."""
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib

app = FastAPI(title="Iris Flower Prediction API", version="1.0.0")
SPECIES = ["setosa", "versicolor", "virginica"]
MODEL_PATH = Path(__file__).parent / "artifacts" / "iris_model.joblib"

class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)

@app.get("/")
def home():
    return {"message": "Iris Flower Prediction API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/model-info")
def model_info():
    return {"model": "RandomForestClassifier", "classes": SPECIES}

@app.post("/predict")
def predict(payload: IrisInput):
    if not MODEL_PATH.exists():
        raise HTTPException(status_code=503, detail="Run train_model.py first")
    model = joblib.load(MODEL_PATH)
    features = [[payload.sepal_length, payload.sepal_width,
                 payload.petal_length, payload.petal_width]]
    index = int(model.predict(features)[0])
    return {"prediction": index, "species": SPECIES[index],
            "confidence": float(max(model.predict_proba(features)[0]))}
