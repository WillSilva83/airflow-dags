# Gerador de DAGs baseado em YAML

## Objetivo

Criar um motor que leia uma definição YAML e gere uma ou mais DAGs do Airflow, incluindo:

- configuração da DAG;
- criação de tasks;
- dependências entre tasks;
- Assets;
- configurações comuns de execução;
- validação de erros antes da publicação.

## Estratégia de evolução

O gerador deve ser implementado somente após a estabilização das DAGs manuais. O YAML deve modelar padrões reais já utilizados no projeto.

## Schema inicial conceitual

```yaml
dag:
  dag_id: exemplo_elt_clientes
  schedule: "@daily"
  start_date: "2025-01-01"
  catchup: false
  tags:
    - elt
    - exemplo

tasks:
  - task_id: extrair_clientes
    type: python
    callable: extrair_clientes

  - task_id: transformar_clientes
    type: python
    callable: transformar_clientes

  - task_id: carregar_clientes
    type: python
    callable: carregar_clientes

dependencies:
  - upstream: extrair_clientes
    downstream: transformar_clientes

  - upstream: transformar_clientes
    downstream: carregar_clientes
```

O exemplo é apenas conceitual. O layout final deverá ser definido após os primeiros casos de uso.

## Perguntas que o schema deverá responder

- Como identificar uma DAG?
- Quais tipos de task serão suportados?
- Como referenciar funções Python?
- Como declarar dependências?
- Como declarar Assets?
- Como configurar retries, pools, callbacks e parâmetros?
- Como representar dependências entre DAGs?
- Como validar o YAML antes da geração?

## Componentes do gerador

### Parser

Responsável por:

- localizar arquivos YAML;
- carregar o conteúdo;
- detectar erros de sintaxe;
- aplicar valores padrão;
- produzir uma estrutura Python tipada.

### Schema e validação

Pode ser implementado com Pydantic, JSON Schema ou dataclasses com validação própria.

Deve detectar:

- `dag_id` ausente ou inválido;
- `task_id` duplicado;
- dependência para task inexistente;
- ciclos no grafo;
- tipo de task não suportado;
- referência a função inexistente;
- Asset duplicado ou malformado.

### Construção do grafo

Responsável por:

- criar a DAG;
- criar as tasks;
- aplicar dependências;
- configurar grupos;
- configurar Assets;
- garantir que o grafo é acíclico.

### Registro de construtores

Novos tipos de task devem ser adicionados por meio de um registro, evitando condicionais espalhados pelo código:

```python
TASK_BUILDERS = {
    "python": build_python_task,
    "empty": build_empty_task,
}
```

### Publicação

A recomendação inicial é gerar arquivos Python durante uma etapa explícita de build ou deploy, em vez de gerar DAGs dinamicamente durante o carregamento do Airflow. Isso facilita:

- debugging;
- testes;
- versionamento dos artefatos;
- diagnóstico de erros no parser do Airflow.

## Requisitos de qualidade

- A geração deve ser determinística.
- A mesma entrada deve produzir o mesmo resultado.
- Erros devem indicar arquivo, campo e motivo.
- O gerador deve ser testável sem depender de um Airflow em execução.
- O contrato dos Assets deve ser separado dos detalhes de implementação da DAG produtora.
