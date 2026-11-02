# Airflow DAGs

Repositório de código-fonte das DAGs para Apache Airflow 3.2.2, evoluindo de DAGs básicas para pipelines ELT e um gerador de DAGs baseado em YAML.

## Responsabilidades deste repositório

- armazenar as DAGs;
- armazenar código reutilizável das DAGs;
- armazenar testes de importação e comportamento;
- armazenar exemplos e configurações relacionadas ao desenvolvimento;
- documentar a evolução dos pipelines.

A infraestrutura de execução não fica neste repositório. O Docker Compose utilizado na
AWS está no projeto [`airflow-aws`](../airflow-aws). Durante o bootstrap da EC2, o
projeto de infraestrutura clona este repositório para `/opt/airflow/dags` e monta esse
diretório nos serviços do Airflow.

## DAG mínima

A DAG `hello_airflow` está em [`dags/hello_airflow.py`](dags/hello_airflow.py). Ela
serve para validar o carregamento e a execução de uma DAG no Airflow 3.2.2.

## Desenvolvimento local

Para executar o ambiente completo localmente, use o Compose do projeto
`airflow-aws`. Configure o diretório de DAGs desse Compose para apontar para este
repositório, por exemplo:

```bash
cd ../airflow-aws
mkdir -p dags
# Alternativa para desenvolvimento local: copie ou sincronize as DAGs
cp ../airflow-dags/dags/*.py dags/
```

Depois, siga as instruções no [`airflow-aws/README.md`](../airflow-aws/README.md).

A infraestrutura da AWS não copia automaticamente alterações locais. Em AWS, uma nova
versão das DAGs deve ser publicada no repositório Git configurado em
`dags_repository_url` e sincronizada na EC2 conforme o processo de deploy definido no
projeto `airflow-aws`.

## Testes

Os testes dependem das bibliotecas do Airflow. Quando executados dentro da imagem do
Airflow, o teste de importação pode ser executado com:

```bash
pytest tests/test_dag_import.py
```

Para validar erros de importação no ambiente em execução:

```bash
docker compose exec airflow-dag-processor airflow dags list-import-errors
```

O comando deve ser executado a partir do diretório do projeto `airflow-aws`, onde o
Compose está localizado.

## Documentação

A documentação detalhada está em [`docs/README.md`](docs/README.md).
