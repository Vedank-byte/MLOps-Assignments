# Assignment 4 — Apache Airflow DAG

**Verified configuration from the assignment report:** Airflow 3.1.3 in Docker, DAG `data_pipeline_dag`, schedule `@daily`, five PythonOperator tasks, ordered as below.

```text
data_extraction >> data_validation >> data_processing >> report_generation >> notification
```

This is a task-dependency excerpt, **not** the complete original `dags/data_pipeline_dag.py`. Recorded run: all five tasks succeeded; generated report contained 5 input records, 1 missing value, 0 invalid records and 5 processed records. Original project: `C:\Users\vedan\Assignment4`.
