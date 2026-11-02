# Milestone 1 — Ambiente funcional

## Status

**Em implementação.**

## Escopo entregue

- Integração com o Docker Compose do projeto `airflow-aws`.
- Airflow 3.2.2 executado pela infraestrutura AWS.
- Repositório de DAGs clonado no bootstrap da EC2.
- DAG mínima `hello_airflow`.
- Teste de importação da DAG.
- README com instruções de integração e operação.

## Critérios de aceite

- [ ] `terraform validate` passa no projeto `airflow-aws`.
- [ ] O `terraform plan` contém a URL e a referência esperadas do repositório de DAGs.
- [ ] O bootstrap clona o repositório em `/opt/airflow/dags`.
- [ ] Os serviços do Airflow montam o diretório clonado.
- [ ] A DAG `hello_airflow` aparece na interface.
- [ ] A DAG executa com sucesso.
- [ ] `list-import-errors` não retorna erros.
- [ ] O teste `tests/test_dag_import.py` passa.
- [ ] O banco mantém os dados após reinicialização da EC2.

## Observação

A validação completa depende de AWS, Docker e de uma URL real do GitHub configurada em `airflow-aws/terraform.tfvars`. O código foi preparado, mas o clone e a execução dos containers devem ser validados após um `terraform plan` aprovado e um deploy controlado.
