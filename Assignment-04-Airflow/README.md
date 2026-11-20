# Assignment 4 — Apache Airflow

**Aim:** Orchestrate extraction, validation, processing, reporting and notification tasks.

**Files:** `dags/data_pipeline_dag.py` is a reconstructed five-stage Airflow DAG; `task_dependencies.txt` records the original task ordering; `requirements.txt` lists Airflow. The original Docker Compose configuration and DAG source are not included.

**Recorded original output:** All five tasks succeeded; 5 input records, 1 missing value, 0 invalid records and 5 processed records. These are documented original observations, not a claim that the reconstructed DAG was executed.
