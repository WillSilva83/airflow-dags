# Infraestrutura e deploy

## Ambiente local

A infraestrutura de execução fica no projeto `airflow-aws`, que mantém o Docker Compose e a configuração da EC2. Para desenvolvimento local, o Compose desse projeto deve montar ou sincronizar o diretório `dags/` deste repositório.

O ambiente de execução oferece:

- Airflow 3.2.2;
- banco de metadados PostgreSQL;
- scheduler;
- API server;
- dag processor;
- triggerer;
- workers Celery;
- Redis;
- health checks;
- persistência do banco;
- usuário administrativo inicial.

Os comandos de operação estão documentados no `README.md` do projeto `airflow-aws`.

## Execução na AWS

O ambiente de homologação será executado em uma EC2. O bootstrap do projeto `airflow-aws` clona o repositório de DAGs configurado em `dags_repository_url` e monta o checkout em `/opt/airflow/dags` nos containers.

### Atividades

- definir sistema operacional e tamanho inicial da instância;
- instalar Docker e Docker Compose;
- configurar armazenamento persistente;
- configurar Security Group;
- restringir o acesso à interface;
- definir backups do banco de metadados;
- configurar monitoramento e logs;
- definir estratégia de atualização e rollback.

### Acesso à interface

Avaliar, preferencialmente nesta ordem:

- VPN;
- túnel SSH;
- proxy reverso com HTTPS;
- acesso público restrito, somente se necessário.

## Segurança

- Nunca versionar secrets.
- Usar `.env` protegido, AWS Secrets Manager ou AWS Systems Manager Parameter Store.
- Restringir o acesso ao banco.
- Não expor portas internas desnecessariamente.
- Definir usuários e permissões do Airflow.
- Revisar permissões IAM da instância.

## Estratégias de deploy

Avaliar as seguintes opções:

- clone controlado do Git na EC2;
- pipeline de CI/CD;
- construção e publicação de imagem Docker;
- sincronização controlada das DAGs.

A estratégia escolhida deve permitir:

- deploy reproduzível;
- identificação da versão em execução;
- rollback para uma versão anterior;
- validação antes da ativação.

## GitHub e CI/CD

Configurar no repositório:

- branch protection;
- pull requests obrigatórios;
- `CODEOWNERS`, se aplicável;
- template de issue;
- template de pull request;
- releases ou changelog.

O deploy deve ocorrer somente após a validação de código, DAGs, YAMLs e testes.
