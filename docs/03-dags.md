# Estrutura e catálogo de DAGs

## Estrutura sugerida

```text
airflow-dags/
├── dags/
│   ├── 01_basicas/
│   ├── 02_dependencias/
│   ├── 03_elt/
│   ├── 04_assets/
│   └── generated/
├── src/
│   └── dag_generator/
├── config/
│   ├── examples/
│   └── schemas/
├── tests/
│   ├── dags/
│   └── generator/
├── plugins/
├── scripts/
├── requirements.txt
├── pyproject.toml
├── .env.example
├── README.md
└── docs/
```

## Princípios

- Manter as DAGs pequenas e legíveis.
- Evitar lógica complexa diretamente nos arquivos de DAG.
- Isolar código reutilizável em `src/`.
- Organizar as DAGs por nível de complexidade e assunto.
- Tratar DAGs geradas como artefatos reproduzíveis.
- Definir convenções de nomes para DAGs, tasks e Assets.

## Níveis de complexidade

### Nível 1 — DAGs básicas

Demonstrar:

- `EmptyOperator`;
- `PythonOperator`;
- sucesso e falha controlados;
- parâmetros da DAG;
- retries;
- timeout e `execution_timeout`;
- agendamento e `catchup`.

### Nível 2 — Dependência entre tasks

Demonstrar:

- dependências lineares;
- branching;
- dynamic task mapping;
- `TaskGroup`;
- trigger rules.

### Nível 3 — ELT simples

Demonstrar:

- extração de CSV ou fonte equivalente;
- transformação em Python ou SQL;
- carregamento em banco;
- validação de dados;
- idempotência;
- tratamento de dados vazios e falhas parciais.

### Nível 4 — Assets

Demonstrar:

- DAG produtora de um Asset;
- DAG consumidora;
- atualização automática baseada em Asset;
- dependência entre DAGs sem acoplamento direto;
- metadados associados aos Assets, quando aplicável.

### Nível 5 — ELT realista

Demonstrar:

- ingestão incremental;
- particionamento;
- cargas full e incremental;
- sensores;
- hooks e connections;
- integrações com serviços AWS;
- retries com backoff;
- observabilidade e alertas.

## Critério de aceite de cada exemplo

Cada nível deve conter:

- pelo menos uma DAG funcional;
- documentação do conceito demonstrado;
- teste de importação;
- dados ou serviços locais suficientes para reprodução.
