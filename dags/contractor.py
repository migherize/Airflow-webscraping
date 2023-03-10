""""
Dags para Airflow Webscraping
author: Miguel Herize
mail: migherize@gmail.com
"""
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
    print("Ejecutar Araña Contractor")


with DAG(
    dag_id="Contractor",
    description="utilizando python operator",
    schedule_interval="@once",
    start_date=datetime(2023, 3, 9),
) as dag:
    op = PythonOperator(task_id="contractor_spider", python_callable=print_hello)
