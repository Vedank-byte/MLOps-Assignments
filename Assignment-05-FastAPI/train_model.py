"""Reconstructed training code based on Assignment 5 report, not exact original file."""
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Test accuracy:", accuracy_score(y_test, model.predict(X_test)))
Path("artifacts").mkdir(exist_ok=True)
joblib.dump(model, "artifacts/iris_model.joblib")
