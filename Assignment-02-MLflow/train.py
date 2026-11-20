"""Reconstructed runnable MLflow comparison; not the original training script."""
from pathlib import Path
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

iris=load_iris(as_frame=True)
X,y=iris.data,iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
mlflow.set_experiment("Iris_Classification_Experiments")
models={"Logistic Regression":LogisticRegression(max_iter=500),
        "Decision Tree":DecisionTreeClassifier(random_state=42),
        "Random Forest":RandomForestClassifier(random_state=42)}
Path("outputs").mkdir(exist_ok=True)
for name,model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train,y_train)
        pred=model.predict(X_test)
        accuracy=accuracy_score(y_test,pred)
        p,r,f,_=precision_recall_fscore_support(y_test,pred,average="weighted",zero_division=0)
        mlflow.log_params(model.get_params())
        mlflow.log_metrics({"accuracy":accuracy,"precision":p,"recall":r,"f1_score":f})
        fig,ax=plt.subplots()
        ConfusionMatrixDisplay.from_predictions(y_test,pred,ax=ax)
        fig.savefig("outputs/confusion_matrix.png",bbox_inches="tight")
        plt.close(fig)
        mlflow.log_artifact("outputs/confusion_matrix.png")
        mlflow.sklearn.log_model(model,name="model")
        print(name,round(accuracy,4))
