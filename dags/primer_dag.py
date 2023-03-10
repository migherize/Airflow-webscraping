""""
Dags para Airflow Webscraping
author: Miguel Herize
mail: migherize@gmail.com
"""
from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dag1",
    description="dag1",
    start_date=datetime(2023, 3, 9),
    schedule_interval="@once",
) as dag1:
    op = EmptyOperator(task_id="dummy")

"""
dag2 = DAG(
    dag_id="dag2",
    description="2dag2",
    start_date=datetime(2023, 3, 9),
    schedule_interval="@once",
)
op2 = EmptyOperator(task_id="dummy2", dag=dag2)


@dag(
    dag_id="dag3",
    description="dag3",
    start_date=datetime(2023, 3, 9),
    schedule_interval="@once",
)
def generate_dag():
    op3 = EmptyOperator(task_id="dummy3")


dag3 = generate_dag()
"""
