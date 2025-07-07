from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.sdk import Variable
from airflow.utils.trigger_rule import TriggerRule


from utils.get_enem_zip_files import baixar_microdados_enem


#========================== Define functions =========================

def extract(**kwargs):
    confs = Variable.get('EXTRACAO', deserialize_json=True)
    return baixar_microdados_enem(ano= confs['ENEM']['ANO'], 
                                  pasta_destino= confs['ENEM']['path'])


#========================== DAGs Definitions =========================

with DAG(
    dag_id='Pipeline',
    schedule='@daily',
    description='Pipeline de dados do processo',
    catchup=False,
    tags=['Pipeline',]
) as dag:
    
    task_download = PythonOperator(
        task_id='dowload',
        python_callable=baixar_microdados_enem
    )

#========================== Task flow =========================
task_download
