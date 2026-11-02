# Visão geral e escopo

## Objetivo do projeto

Criar uma estrutura inicial de DAGs para o Apache Airflow 3.2.2 com os seguintes objetivos:

- testar novas funcionalidades do Airflow;
- apresentar DAGs do nível mais simples ao mais complexo;
- demonstrar padrões de engenharia de dados, principalmente ELT;
- criar posteriormente um motor que gere `N` DAGs a partir de YAML;
- permitir dependências entre tasks e comunicação entre DAGs por meio de Assets;
- manter o projeto versionado no GitHub;
- executar o ambiente Airflow em uma EC2 na AWS usando Docker Compose.

## Escopo inicial

O projeto deverá contemplar:

- ambiente local reproduzível;
- catálogo progressivo de DAGs de exemplo;
- pipelines ELT idempotentes;
- exemplos de Assets;
- gerador de DAGs orientado a YAML;
- testes automatizados;
- documentação de operação e deploy;
- preparação para execução na AWS.

## Decisões ainda pendentes

Antes da implementação definitiva, devem ser definidos:

- executor do Airflow: `LocalExecutor`, `CeleryExecutor` ou outro;
- banco de metadados, com PostgreSQL como opção recomendada;
- estratégia de geração das DAGs: durante o build/deploy ou em tempo de carregamento;
- forma de armazenamento de secrets;
- estratégia de acesso à interface do Airflow na EC2;
- convenções finais de nomes para DAGs, tasks e Assets.

## Critérios de sucesso

- O ambiente sobe localmente com um procedimento documentado.
- O Airflow executa uma DAG mínima.
- O repositório possui DAGs organizadas por nível de complexidade.
- Existe pelo menos um fluxo ELT funcional e idempotente.
- Existe um exemplo de DAG produtora e DAG consumidora usando Assets.
- Um YAML válido gera uma DAG executável.
- YAMLs inválidos produzem mensagens de erro claras.
- O CI valida DAGs, YAMLs e testes antes do deploy.
- O ambiente da EC2 pode ser atualizado de forma reproduzível.
