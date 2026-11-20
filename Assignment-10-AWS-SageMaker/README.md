# Assignment 10 — AWS SageMaker Deployment

**Aim:** Train an Iris classifier in AWS SageMaker and deploy an XGBoost serverless inference endpoint.

**Files:** [random_forest_baseline_excerpt.py](random_forest_baseline_excerpt.py), [xgboost_train_excerpt.py](xgboost_train_excerpt.py), and [invoke_endpoint_excerpt.py](invoke_endpoint_excerpt.py). These are **not complete standalone programs**; they require the original notebook, AWS resources and setup.

**Recorded output:** SageMaker `ml.t3.medium` notebook **InService**; XGBoost serverless endpoint `iris-xgboost-endpoint` **InService**; successful cloud inference returned **0.0 (Setosa)**. The **100% test accuracy** was measured for the initial Random Forest, **not** the final XGBoost model.

**Original assignment repository:** https://github.com/Hidden-primacy/AWS-SageMaker-ML-Deployment

AWS credentials and original cloud artifacts are not included. Original console screenshots have not been uploaded here.
