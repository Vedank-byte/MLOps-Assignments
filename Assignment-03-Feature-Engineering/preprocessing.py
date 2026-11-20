"""Reconstructed Titanic preprocessing module based on assignment report."""
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler

NUMERIC=["Age","SibSp","Parch","Fare"]
CATEGORICAL=["Pclass","Sex","Embarked"]

def build_preprocessor():
    numeric=Pipeline([("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())])
    categorical=Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),
                          ("encoder",OneHotEncoder(handle_unknown="ignore",sparse_output=False))])
    return ColumnTransformer([("numeric",numeric,NUMERIC),("categorical",categorical,CATEGORICAL)])
