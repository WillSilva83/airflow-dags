# Roadmap e milestones

## Milestone 1 — Ambiente funcional

- Validar o Docker Compose existente.
- Fixar e confirmar o Airflow 3.2.2.
- Criar uma DAG mínima.
- Documentar a execução local.
- Confirmar persistência do banco de metadados.

**Resultado esperado:** ambiente local acessível e capaz de executar uma DAG.

## Milestone 2 — Catálogo inicial de DAGs

- Criar DAGs básicas.
- Demonstrar dependências entre tasks.
- Adicionar retries, timeouts, parâmetros e `catchup`.
- Demonstrar branching, `TaskGroup` e dynamic task mapping.
- Criar testes de importação.

**Resultado esperado:** catálogo organizado dos conceitos fundamentais do Airflow.

## Milestone 3 — Primeiro fluxo ELT

- Implementar extração.
- Implementar transformação.
- Implementar carga.
- Adicionar validação de dados.
- Tratar dados vazios e falhas parciais.
- Garantir idempotência.

**Resultado esperado:** pipeline ELT completo e reproduzível.

## Milestone 4 — Assets

- Criar uma DAG produtora de Asset.
- Criar uma DAG consumidora.
- Validar a execução orientada à atualização do Asset.
- Documentar Assets versus dependências entre tasks e `TriggerDagRunOperator`.

**Resultado esperado:** comunicação desacoplada entre DAGs usando Assets.

## Milestone 5 — Gerador YAML mínimo

- Definir o primeiro schema YAML.
- Implementar parser.
- Validar o schema.
- Gerar DAGs com tasks simples e dependências.
- Criar testes unitários.

**Resultado esperado:** um YAML válido gera uma DAG funcional.

## Milestone 6 — Gerador completo

- Suportar múltiplos tipos de tasks.
- Suportar Assets.
- Validar o grafo e detectar ciclos.
- Adicionar geração determinística.
- Implementar registro extensível de construtores de tasks.
- Ampliar a cobertura de testes.

**Resultado esperado:** motor capaz de representar os principais padrões do catálogo de DAGs.

## Milestone 7 — GitHub, AWS e CI/CD

- Publicar e organizar o repositório no GitHub.
- Configurar lint, validação de YAML e testes no CI.
- Preparar a EC2.
- Automatizar o deploy.
- Configurar persistência, segurança e observabilidade.
- Definir rollback.

**Resultado esperado:** execução operacional reproduzível na AWS.

## Primeiras tarefas práticas

1. Inspecionar o Docker Compose existente e confirmar a versão do Airflow.
2. Criar a estrutura de diretórios do repositório.
3. Adicionar uma DAG mínima e um teste de importação.
4. Documentar o procedimento local no `README.md`.
5. Criar as primeiras DAGs básicas.
6. Implementar um fluxo ELT simples.
7. Criar o primeiro exemplo com Assets.
8. Definir e implementar o schema YAML inicial.
9. Automatizar a validação no CI.
10. Preparar o deploy na EC2.
