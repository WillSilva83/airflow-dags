# Testes e qualidade

## Testes de DAGs

Criar testes para verificar:

- importação de todos os arquivos de DAG;
- ausência de erros durante o carregamento;
- IDs únicos;
- presença das tasks esperadas;
- dependências esperadas;
- ausência de ciclos;
- configurações críticas.

## Testes do gerador

Cobrir pelo menos os cenários abaixo:

- YAML válido gera a DAG esperada;
- YAML inválido retorna erro claro;
- `task_id` duplicado é rejeitado;
- dependência para task inexistente é rejeitada;
- referência de função inexistente é rejeitada;
- ciclos no grafo são rejeitados;
- Assets produtores e consumidores são relacionados corretamente;
- mesma entrada produz saída determinística.

## Testes de integração

Validar, em ambiente Airflow:

- subida dos serviços;
- registro de uma DAG gerada;
- execução de uma DAG simples;
- atualização de um Asset;
- acionamento da DAG consumidora.

## Qualidade no CI

O pipeline do GitHub deverá:

1. instalar as dependências;
2. executar lint e formatação;
3. validar os arquivos YAML;
4. importar todas as DAGs;
5. executar testes unitários;
6. validar os artefatos gerados;
7. opcionalmente construir a imagem Docker;
8. fazer deploy somente após aprovação.

## Boas práticas

- Preferir testes determinísticos.
- Evitar dependência de serviços externos nos testes unitários.
- Usar fixtures para dados de entrada.
- Testar mensagens de erro, não apenas o fato de uma exceção ocorrer.
- Separar testes unitários, de DAGs e de integração.
- Executar localmente os mesmos comandos essenciais do CI.
