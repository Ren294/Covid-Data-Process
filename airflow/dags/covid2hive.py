from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    'owner': 'ren294',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'covid2hive',
    default_args=default_args,
    description='A DAG to run Spark jobs Covid Data to Hive',
    schedule_interval='0 0 * * *',
    start_date=datetime.now(),
    catchup=False
)
spark_submit_command = '/opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/spark-apps/data2hive.py'

data2hive_task = SSHOperator(
    task_id='process2hive',
    ssh_conn_id='spark_conn',
    command=spark_submit_command,
    dag=dag,
)
data2hive_task
