# Documentação do projeto

## Objetivo

Este projeto é um laboratório de DAGs para o Apache Airflow 3.2.2, evoluindo de exemplos simples para pipelines de engenharia de dados mais completos. Em uma segunda etapa, o projeto terá um motor capaz de gerar múltiplas DAGs a partir de arquivos YAML.

## Navegação

- [Visão geral e escopo](01-visao-geral.md)
- [Roadmap e milestones](02-roadmap.md)
- [Milestone 1 — Ambiente funcional](08-milestone-1.md)
- [Estrutura e catálogo de DAGs](03-dags.md)
- [Gerador de DAGs baseado em YAML](04-gerador-yaml.md)
- [Assets e comunicação entre DAGs](05-assets.md)
- [Testes e qualidade](06-testes.md)
- [Infraestrutura e deploy](07-infraestrutura.md)

## Ordem recomendada de leitura

1. [Milestone 1 — Ambiente funcional](08-milestone-1.md)
2. [Visão geral e escopo](01-visao-geral.md)
3. [Roadmap e milestones](02-roadmap.md)
4. [Estrutura e catálogo de DAGs](03-dags.md)
5. [Gerador de DAGs baseado em YAML](04-gerador-yaml.md)
6. [Assets e comunicação entre DAGs](05-assets.md)
7. [Testes e qualidade](06-testes.md)
8. [Infraestrutura e deploy](07-infraestrutura.md)

## Princípio de evolução

A implementação deve começar pelas DAGs manuais e pelos padrões de ELT. O gerador YAML só deve ser abstraído depois que os casos reais estiverem estáveis. Dessa forma, o schema será baseado em necessidades comprovadas e não em uma abstração especulativa.
