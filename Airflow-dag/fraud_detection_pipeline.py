from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os
import subprocess

default_args = {
    'owner': 'youcode2',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 5),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'test_single_script1',
    default_args=default_args,
    schedule_interval='@daily',
)

# Use the correct directory name
script_directory = '/opt/airflow/dags/brief-hadoop-fraud'
script_path = f'{script_directory}/load_customers.py'

def run_script():
    try:
        # Debug prints
        print(f'Script Directory: {script_directory}')
        print(f'Script Path: {script_path}')
        print(f'Found local files: {os.listdir(script_directory)}')

        # Execute the script using subprocess
        subprocess.run(['python', script_path])
    except Exception as e:
        # Print the exception for debugging
        print(f'Error executing script: {e}')
        raise

run_single_script = PythonOperator(
    task_id='run_single_script',
    python_callable=run_script,
    dag=dag,
)

run_single_script
