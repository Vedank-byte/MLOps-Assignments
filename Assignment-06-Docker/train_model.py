"""Reconstructed model generation to make the documented Flask container reproducible."""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
iris = load_iris()
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(iris.data, iris.target)
joblib.dump(model, "iris_model.pkl")
print("Saved iris_model.pkl")
