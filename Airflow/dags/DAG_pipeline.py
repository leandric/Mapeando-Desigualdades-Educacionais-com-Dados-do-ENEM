from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow.models import Variable
from airflow.utils.trigger_rule import TriggerRule

from utils.unzip import extrair_zips
from utils.get_enem_zip_files import baixar_microdados_enem

#========================== Define functions =========================

def extract(**kwargs):
    confs = Variable.get('EXTRACAO', deserialize_json=True)
    print('=================================================', confs)
    return baixar_microdados_enem(
        ano=confs['ENEM']['ANO'], 
        pasta_destino=confs['ENEM']['PATH']
    )

def unzip(**kwargs):
    ti = kwargs['ti']
    file_path = ti.xcom_pull(task_ids='download')
    print(f"📦 Extraindo: {file_path}")
    extrair_zips(file_path, file_path)

#========================== DAGs Definitions =========================

with DAG(
    dag_id='Pipeline',
    schedule='@daily',
    description='Pipeline de dados do processo',
    catchup=False,
    tags=['Pipeline'],
) as dag:

    task_download = PythonOperator(
        task_id='download',
        python_callable=extract,
    )

    task_unzip = PythonOperator(
        task_id='unzip',
        python_callable=unzip,
    )

    #========================== Task flow =========================
    task_download >> task_unzip
