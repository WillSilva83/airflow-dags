"""DAG mínima para validar o ambiente local do Airflow."""

from datetime import datetime

from airflow.sdk import dag, task

@dag(
    dag_id="hello_airflow",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["milestone-1", "basica"],
    doc_md="DAG mínima usada para validar a instalação local do Airflow.",
)
def hello_airflow():
    @task
    def dizer_ola() -> str:
        mensagem = "Airflow 3.2.2 funcionando"
        print(mensagem)
        return mensagem

    dizer_ola()


hello_airflow()
