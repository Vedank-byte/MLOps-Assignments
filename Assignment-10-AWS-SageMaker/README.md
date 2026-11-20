# Assignment 10 — AWS SageMaker Iris Deployment

**Existing assignment-specific repository:** https://github.com/Hidden-primacy/AWS-SageMaker-ML-Deployment

This directory contains only **documented code excerpts**. It does not contain a complete runnable cloud deployment, because AWS account configuration, S3 object locations, training/deployment model setup and original notebook are not available here.

**Baseline Random Forest (100% test accuracy on 30 samples, not the final XGBoost accuracy):**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
joblib.dump(model, "model.joblib")
```

**Final XGBoost excerpts:**

```python
model = xgb.XGBClassifier(n_estimators=50, max_depth=3,
    objective="multi:softmax", num_class=3, random_state=42, n_jobs=2)
model.fit(X_train.to_numpy(), y_train)
model.get_booster().save_model("xgboost-model.json")
deployment_model.deploy(serverless_inference_config=serverless_config,
    endpoint_name="iris-xgboost-endpoint")
```

**Verified endpoint invocation:**

```python
runtime = boto3.client("sagemaker-runtime")
response = runtime.invoke_endpoint(
    EndpointName="iris-xgboost-endpoint",
    ContentType="text/csv", Accept="text/csv",
    Body=b"5.1,3.5,1.4,0.2")
result = response["Body"].read().decode()
predicted_class = int(float(result.strip().strip('[]')))
print("Endpoint prediction:", result)
print("Predicted flower:", iris.target_names[predicted_class])
```

Evidence: `ml.t3.medium` notebook `InService`, XGBoost **serverless** endpoint `iris-xgboost-endpoint` `InService`, successful inference **0.0 / Setosa**. The XGBoost test accuracy was not established by the supplied screenshots. No AWS credentials are stored in this repository.
