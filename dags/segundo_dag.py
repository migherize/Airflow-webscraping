""""
Dags para Airflow Webscraping
author: Miguel Herize
mail: migherize@gmail.com
"""
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="bashoperator",
    description="utilizando bash operator",
    start_date=datetime(2023, 3, 9),
) as dag:
    op = BashOperator(task_id="Hello_with_bash", bash_command="echo 'Hello miguel'")
