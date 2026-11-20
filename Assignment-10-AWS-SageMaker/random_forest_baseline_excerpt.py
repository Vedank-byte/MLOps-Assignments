"""Preserved notebook excerpt; requires X_train, X_test, y_train, y_test."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
joblib.dump(model, "model.joblib")
