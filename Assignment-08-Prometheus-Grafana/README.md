# Assignment 8 — Prometheus & Grafana Monitoring

**Verified from the completed practical:**

```text
POST http://127.0.0.1:8001/predict
GET  http://127.0.0.1:8001/metrics/
Prometheus scrape: host.docker.internal:8001/metrics/
Prometheus job: iris-ml-api
```

**PromQL queries used:**

```promql
sum(iris_predictions_total)
sum(rate(iris_http_requests_total{endpoint="/predict"}[5m]))
up{job="iris-ml-api"}
```

The Grafana dashboard showed **52 total predictions** after a batch of 50 additional requests, with a nonzero request rate. Prometheus showed target health **UP (1/1)**. Full local API and Docker Compose configuration were not provided as source attachments, so this directory does not claim to contain them.
