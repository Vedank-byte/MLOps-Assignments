# Flask service excerpt from the report; model artifact not included.
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
