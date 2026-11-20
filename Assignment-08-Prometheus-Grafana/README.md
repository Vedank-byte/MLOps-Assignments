# Assignment 8 — Monitor an Iris ML API with Prometheus and Grafana

**Purpose:** Serve an Iris classifier, collect Prometheus metrics and visualize prediction volume, request throughput and scrape health in Grafana.

## Project files

- `app.py` — FastAPI prediction endpoint and Prometheus counters
- `train_model.py` — creates the local Iris model artifact
- `requirements.txt` — Python dependencies
- `prometheus.yml` — Prometheus scrape configuration
- `docker-compose.yml` — Prometheus and Grafana containers
- `generate_requests.ps1` — sends 50 prediction requests
- `grafana-queries.promql` — three dashboard queries

**Source status:** The Python and container configuration files above are **reconstructed implementations** based on the recorded assignment behavior, not copies of the original local files. The observed endpoint paths, metric names, scrape target, queries and results are taken from the practical report.

## Recorded output / results

| Observation | Recorded result |
| --- | --- |
| Initial prediction count | **2** |
| Additional prediction requests | **50** |
| Final Grafana prediction count | **52** |
| Prometheus target | **UP (1/1)** |
| Grafana request-rate graph | Rose above zero after traffic |
| API | `POST http://127.0.0.1:8001/predict` |
| Metrics | `GET http://127.0.0.1:8001/metrics/` |

**The 2 → 52 results are from the original run, not a guaranteed starting value for this reconstructed implementation.** Counters reset when the API process restarts. The original dashboard screenshot has not been uploaded to this GitHub folder yet; do not mistake the results table for an actual graph image.

## Run locally

```powershell
python -m pip install -r requirements.txt
python train_model.py
python -m uvicorn app:app --host 0.0.0.0 --port 8001
```

In a second PowerShell window, run `docker compose up -d`. Open Prometheus at http://localhost:9090 and Grafana at http://localhost:3000. Configure Grafana's Prometheus data source URL as `http://prometheus:9090`, then create the panels using `grafana-queries.promql`. To reproduce the traffic batch, run `.\\generate_requests.ps1` in a third window. Default Grafana credentials in the sample Compose file are for **local development only**; change them for any shared deployment.

## Scope

This exercise verifies operational counters and scrape reachability. It does not establish model accuracy, drift, P95 latency, or production reliability.
