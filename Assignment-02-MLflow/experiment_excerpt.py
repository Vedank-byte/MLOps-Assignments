"""Code excerpt from the HA report; requires model definitions, data and imports."""
df = pd.read_csv("data/iris.csv").dropna()
X, y = df.drop(columns=["target"]), df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
mlflow.set_experiment("Iris_Classification_Experiments")
# Inside each MLflow run after fitting model and calculating metrics:
mlflow.log_params(model.get_params())
mlflow.log_metrics({
    "accuracy": accuracy, "precision": precision,
    "recall": recall, "f1_score": f1
})
mlflow.log_artifact(confusion_matrix_png)
mlflow.log_artifact(classification_report_txt)
mlflow.sklearn.log_model(sk_model=model, name="model",
    input_example=X_train.head(3),
    skops_trusted_types=["sklearn.tree._tree.Tree"])
