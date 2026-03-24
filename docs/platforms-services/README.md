# Evolução de Plataformas de IA na Nuvem

A adoção de Inteligência Artificial na nuvem não acontece de uma vez. Ela segue uma jornada de maturidade que pode ser dividida em três níveis, onde cada etapa traz mais automação, menos complexidade operacional e maior foco no negócio.

## Visão Geral da Evolução

```
┌─────────────────────────────┐
│  Nível 3: Aplicações de IA  │  ← Foco no negócio
│  Bedrock, Agentes, RAG,     │
│  Serverless                  │
├─────────────────────────────┤
│  Nível 2: Serviços de ML    │  ← Foco em modelos
│  SageMaker, Pipelines,      │
│  Treinamento gerenciado      │
├─────────────────────────────┤
│  Nível 1: Infraestrutura    │  ← Foco em infra (estamos aqui!)
│  EC2, Object Storage,       │
│  RDS, GPUs                   │
└─────────────────────────────┘
```

Cada nível se apoia no anterior. Não é necessário abandonar um nível para avançar ao próximo — eles coexistem.

## Comparativo

| Aspecto | Nível 1 | Nível 2 | Nível 3 |
|---------|---------|---------|---------|
| Foco | Infraestrutura | Modelos de ML | Aplicações inteligentes |
| Controle | Total | Parcial | Mínimo |
| Complexidade operacional | Alta | Média | Baixa |
| Time-to-market | Lento | Moderado | Rápido |
| Customização | Máxima | Alta | Limitada |
| Exemplos de serviços | EC2, RDS, S3 | SageMaker, Glue | Bedrock, AI Services |

## Onde estamos neste curso?

Neste curso, trabalhamos no **Nível 1**: criamos uma instância EC2, configuramos um banco PostgreSQL no RDS e subimos uma API Flask. Essa é a base sobre a qual os níveis mais avançados são construídos.

## Detalhamento por Nível

- [Nível 1 — Hardware e Infraestrutura](nivel_1.md)
- [Nível 2 — Modelos e Serviços de ML](nivel_2.md)
- [Nível 3 — Aplicações e Serviços de IA](nivel_3.md)
