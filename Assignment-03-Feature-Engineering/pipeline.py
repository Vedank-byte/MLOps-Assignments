"""Reconstructed executable pipeline; requires your own Titanic train.csv."""
from pathlib import Path
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from preprocessing import build_preprocessor,NUMERIC,CATEGORICAL
from feature_selection import build_selector

path=Path("data/train.csv")
if not path.exists():
    raise FileNotFoundError("Place the original Titanic train.csv at data/train.csv")
df=pd.read_csv(path)
X=df[NUMERIC+CATEGORICAL]
y=df["Survived"]
pipeline=Pipeline([("preprocessor",build_preprocessor()),("feature_selection",build_selector())])
features=pipeline.fit_transform(X,y)
Path("models").mkdir(exist_ok=True)
joblib.dump(pipeline,"models/feature_pipeline.pkl")
print("Transformed shape:",features.shape)
print("Selected:",pipeline.named_steps["preprocessor"].get_feature_names_out()[pipeline.named_steps["feature_selection"].get_support()])
