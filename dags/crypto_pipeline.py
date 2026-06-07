from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add the scripts folder to path
sys.path.append('/opt/airflow/project-4-crypto-pipeline/scripts')

from extract import fetch_crypto_prices, load_to_postgres
from crypto_signal import detect_price_drop

def run_extraction():
    data = fetch_crypto_prices()
    load_to_postgres(data)

default_args = {
    'owner': 'priyanka',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 0,
}

with DAG(
    'crypto_monitoring_pipeline',
    default_args=default_args,
    description='Near real-time crypto price monitoring',
    schedule_interval='* * * * *',
    catchup=False
) as dag:

    task_fetch_load = PythonOperator(
        task_id='fetch_and_load_prices',
        python_callable=run_extraction
    )

    task_detect_signal = PythonOperator(
        task_id='detect_price_signals',
        python_callable=detect_price_drop
    )

    task_fetch_load >> task_detect_signal
