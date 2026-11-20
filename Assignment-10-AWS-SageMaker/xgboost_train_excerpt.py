"""Preserved notebook excerpt. Requires X_train, y_train and xgboost import."""
import xgboost as xgb
model = xgb.XGBClassifier(n_estimators=50, max_depth=3,
    objective="multi:softmax", num_class=3, random_state=42, n_jobs=2)
model.fit(X_train.to_numpy(), y_train)
model.get_booster().save_model("xgboost-model.json")
# Deployment requires deployment_model and serverless_config configured in AWS.
deployment_model.deploy(serverless_inference_config=serverless_config,
    endpoint_name="iris-xgboost-endpoint")
