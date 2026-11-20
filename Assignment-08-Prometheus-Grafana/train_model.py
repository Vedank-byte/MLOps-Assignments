"""Reconstructed training utility; the original model binary was not provided."""
from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(iris.data, iris.target)
joblib.dump(model, Path(__file__).parent / "iris_model.joblib")
print("Saved iris_model.joblib")
