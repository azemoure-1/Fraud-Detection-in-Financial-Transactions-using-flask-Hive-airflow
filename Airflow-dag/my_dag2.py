from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os

default_args = {
    'owner': 'Amine',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 5),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'brief_hadoop_fraud',
    default_args=default_args,
    schedule_interval='@daily',
)

script_directory = '/opt/airflow/dags/brief-hadoop-fraud'

# First group of tasks
load_customers_task = PythonOperator(
    task_id='load_customers',
    python_callable=lambda: exec(open(os.path.join(script_directory, 'load_customers.py')).read()),
    dag=dag,
)

load_transactions_task = PythonOperator(
    task_id='load_transactions',
    python_callable=lambda: exec(open(os.path.join(script_directory, 'load_transactions.py')).read()),
    dag=dag,
)

load_external_data_task = PythonOperator(
    task_id='load_external_data',
    python_callable=lambda: exec(open(os.path.join(script_directory, 'load_external_data.py')).read()),
    dag=dag,
)

# Second group of tasks
high_value_task = PythonOperator(
    task_id='high_value',
    python_callable=lambda: exec(open(os.path.join(script_directory, 'High-Value.py')).read()),
    dag=dag,
)

unusual_transaction_task = PythonOperator(
    task_id='unusual_transaction',
    python_callable=lambda: exec(open(os.path.join(script_directory, 'unusual_transaction.py')).read()),
    dag=dag,
)

high_risk_customers_task = PythonOperator(
    task_id='high_risk_customers',
    python_callable=lambda: exec(open(os.path.join(script_directory, 'high_risk_customers.py')).read()),
    dag=dag,
)

suspicious_locations_task = PythonOperator(
    task_id='suspicious_locations',
    python_callable=lambda: exec(open(os.path.join(script_directory, 'suspicious_locations.py')).read()),
    dag=dag,
)

# Define task dependencies
[load_customers_task, load_transactions_task, load_external_data_task] >> high_value_task
[high_value_task, unusual_transaction_task, high_risk_customers_task] >> suspicious_locations_task
