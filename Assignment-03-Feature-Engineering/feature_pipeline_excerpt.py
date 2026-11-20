"""Preserved preprocessing and feature-selection excerpt; imports and data setup omitted."""
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])
preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, ["Age", "SibSp", "Parch", "Fare"]),
    ("categorical", categorical_pipeline, ["Pclass", "Sex", "Embarked"])
])
selector = SelectKBest(score_func=f_classif, k=8)
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("feature_selection", selector)
])
transformed = pipeline.fit_transform(X, y)
selected_names = pipeline.named_steps["preprocessor"].get_feature_names_out()[
    pipeline.named_steps["feature_selection"].get_support()
]
joblib.dump(pipeline, "models/feature_pipeline.pkl")
loaded_pipeline = joblib.load("models/feature_pipeline.pkl")
new_result = loaded_pipeline.transform(sample)
