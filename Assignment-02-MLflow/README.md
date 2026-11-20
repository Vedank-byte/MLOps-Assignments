# Assignment 2 — MLflow Iris Experiments

**Documented implementation excerpts** (not the full original `src/train.py`):

```python
df = pd.read_csv("data/iris.csv").dropna()
X, y = df.drop(columns=["target"]), df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
mlflow.set_experiment("Iris_Classification_Experiments")
# Each model is fitted, evaluated and logged inside mlflow.start_run(run_name=name).
mlflow.log_params(model.get_params())
mlflow.log_metrics({
    "accuracy": accuracy, "precision": precision,
    "recall": recall, "f1_score": f1
})
mlflow.log_artifact(confusion_matrix_png)
mlflow.log_artifact(classification_report_txt)
mlflow.sklearn.log_model(
    sk_model=model, name="model", input_example=X_train.head(3),
    skops_trusted_types=["sklearn.tree._tree.Tree"])
```

Models compared: Logistic Regression, Decision Tree, Random Forest. Recorded test accuracies: 0.9333, 0.9667, 0.9000 respectively. Best model registered as `IrisBestModel`, version 1. Original project location: `C:\Users\vedan\MLflow_Assignment`. Imports, model definitions and artifact generation are omitted from the preserved excerpt.
