# Assignment 6 — Dockerized Iris Classifier

**Aim:** Package an Iris model-serving application in a Docker image.

**Files:** [app.py](app.py) is the preserved Flask API excerpt; [Dockerfile](Dockerfile) is the documented container configuration; [requirements.txt](requirements.txt) lists dependencies; [train_model.py](train_model.py) is a **reconstructed** artifact-generation helper. The original CLI-image source was not available.

**Recorded output:** The separate image `iris-ml-model` successfully predicted **Setosa** for input `[5.1, 3.5, 1.4, 0.2]`. This output belongs to the original CLI test, not necessarily to the Flask image in this folder. Original screenshots and model binary are not included.
