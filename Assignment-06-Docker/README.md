# Assignment 6 — Dockerized Iris Model

The assignment report documents two Docker-related components. The following is a **preserved Flask service excerpt**; it is not proof that this exact service was the final CLI image.

```python
from flask import Flask, request, jsonify
import joblib
app = Flask(__name__)
model = joblib.load("iris_model.pkl")
species = ["setosa", "versicolor", "virginica"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Iris Prediction API using Flask and Docker"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or "features" not in data:
        return jsonify({"error": "Provide features"}), 400
    features = data["features"]
    if not isinstance(features, list) or len(features) != 4 or any(
        not isinstance(x, (int, float)) or isinstance(x, bool) or x <= 0
        for x in features
    ):
        return jsonify({"error": "Four positive numeric features required"}), 400
    label = int(model.predict([features])[0])
    return jsonify({"prediction": label, "species": species[label]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**Documented Flask Dockerfile:**

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY iris_model.pkl .
EXPOSE 5000
CMD ["python", "app.py"]
```

The successful separate Docker CLI test used image `iris-ml-model` and predicted Setosa for `[5.1, 3.5, 1.4, 0.2]`. The original model binary is not included. Local project: `C:\Users\vedan\Assignment6_2`.
