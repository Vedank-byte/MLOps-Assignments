# Assignment 5 — Iris Prediction API with FastAPI

**Aim:** Train an Iris classifier and serve predictions over HTTP.

**Files:** [train_model.py](train_model.py), [main.py](main.py), [requirements.txt](requirements.txt), and [tests/test_api.py](tests/test_api.py). These are **reconstructed from the documented design**, not exact original project files.

**Recorded output:** The original report states **90% test accuracy** and a successful Setosa prediction. The reconstructed training script may produce a different score and must not be represented as the original execution. Original screenshots are not yet included.

**Run:** Install requirements, run `python train_model.py`, then `uvicorn main:app --reload`; run `pytest` after generating the model.
