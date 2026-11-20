"""Reconstructed example DAG matching the documented five-task flow.
Not the exact original DAG file. Airflow 3.x compatible imports.
"""
from datetime import datetime
from airflow.sdk import dag,task

@dag(dag_id="data_pipeline_dag",schedule="@daily",start_date=datetime(2026,1,1),catchup=False)
def data_pipeline():
    @task
    def data_extraction():
        return [{"id":1,"value":10},{"id":2,"value":None},{"id":3,"value":30},
                {"id":4,"value":40},{"id":5,"value":50}]
    @task
    def data_validation(records):
        return {"records":records,"missing":sum(x["value"] is None for x in records)}
    @task
    def data_processing(result):
        records=result["records"]
        values=[x["value"] for x in records if x["value"] is not None]
        replacement=sum(values)/len(values)
        return [{**x,"value":replacement if x["value"] is None else x["value"]} for x in records]
    @task
    def report_generation(records):
        return {"processed_records":len(records),"invalid_records":0}
    @task
    def notification(report):
        print("Pipeline completed:",report)
    notification(report_generation(data_processing(data_validation(data_extraction()))))

data_pipeline()
