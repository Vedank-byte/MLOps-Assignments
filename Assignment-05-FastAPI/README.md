# Assignment 5 — FastAPI Iris Prediction API

**Preserved project outline**, not a complete original source export:

- `train_model.py`: `load_iris()`, 80/20 stratified split (`random_state=42`), `RandomForestClassifier(n_estimators=100, random_state=42)`, save with `joblib.dump(model, "artifacts/iris_model.joblib")`.
- `main.py`: `FastAPI(title="Iris Flower Prediction API", version="1.0.0")`; Pydantic `IrisInput` with four positive float fields; GET `/`, `/health`, `/model-info`; POST `/predict` using `predict` and `predict_proba`.
- `tests/test_api.py`: five `TestClient` checks for valid routes, Setosa prediction, and HTTP 422 for invalid negative input.
- Dependencies: `fastapi[standard]`, `scikit-learn`, `numpy`, `joblib`, `pytest`, `httpx`.

Recorded held-out accuracy: **90%**. The displayed prediction confidence of 1.0 for one Setosa request is **not** overall accuracy. Original local project: `C:\Users\vedan\Assignment5`.
