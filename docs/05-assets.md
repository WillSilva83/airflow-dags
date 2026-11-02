# Assets e comunicação entre DAGs

## Objetivo

Usar Assets para representar contratos de dados e permitir que uma DAG consumidora seja executada quando uma DAG produtora atualizar um dado.

## Conceitos a demonstrar

- Asset produzido por uma DAG.
- Asset consumido por outra DAG.
- Execução orientada à atualização de um Asset.
- Metadados associados ao Asset, quando aplicável.
- Separação entre dependências internas e dependências entre DAGs.

## Diferenças importantes

### Dependência entre tasks

Representa a ordem de execução dentro da mesma DAG. Exemplo: extração antes da transformação.

### Assets

Representam dados ou eventos produzidos por um pipeline e consumidos por outro. O consumidor depende da atualização do dado, não de uma chamada direta à DAG produtora.

### `TriggerDagRunOperator`

Dispara explicitamente outra DAG. Pode ser útil em alguns fluxos, mas cria maior acoplamento entre os pipelines.

## Implementação planejada

1. Criar uma DAG produtora.
2. Definir o Asset gerado pela etapa de carga.
3. Criar uma DAG consumidora orientada ao Asset.
4. Executar o fluxo localmente.
5. Validar a atualização do Asset.
6. Documentar o relacionamento produtor/consumidor.
7. Adicionar suporte a Assets no gerador YAML.

## Convenções a definir

- padrão de nomes dos Assets;
- forma de representar URI ou identificador lógico;
- ownership do contrato;
- metadados obrigatórios;
- tratamento de falha na produção;
- compatibilidade entre versões do schema do dado.

## Critérios de aceite

- A DAG produtora atualiza o Asset somente após a carga bem-sucedida.
- A DAG consumidora não é executada quando a produção falha.
- O relacionamento produtor/consumidor pode ser validado por teste.
- O YAML consegue representar o Asset sem acoplar detalhes desnecessários da implementação.
