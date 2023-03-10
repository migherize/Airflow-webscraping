""""
Dags para Airflow Webscraping
author: Miguel Herize
mail: migherize@gmail.com
"""
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
    print("hello de nuevo miguel")


with DAG(
    dag_id="pythonoperator",
    description="utilizando python operator",
    schedule_interval="@once",
    start_date=datetime(2023, 3, 9),
) as dag:
    op = PythonOperator(task_id="Hello_with_python", python_callable=print_hello)
