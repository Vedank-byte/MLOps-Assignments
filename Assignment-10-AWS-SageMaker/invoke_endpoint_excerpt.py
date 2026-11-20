"""Preserved endpoint invocation excerpt; requires configured AWS credentials and an existing endpoint."""
import boto3
runtime = boto3.client("sagemaker-runtime")
response = runtime.invoke_endpoint(
    EndpointName="iris-xgboost-endpoint",
    ContentType="text/csv", Accept="text/csv",
    Body=b"5.1,3.5,1.4,0.2")
result = response["Body"].read().decode()
predicted_class = int(float(result.strip().strip('[]')))
print("Endpoint prediction:", result)
print("Predicted class index:", predicted_class)
