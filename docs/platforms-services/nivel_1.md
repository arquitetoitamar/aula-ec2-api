# Nível 1: Hardware e Infraestrutura

Este é o ponto de partida da jornada. A empresa monta sua própria stack de IA usando recursos básicos da nuvem e é responsável por toda a configuração, integração e operação.

## Componentes típicos

| Serviço | Função |
|---------|--------|
| EC2 (com ou sem GPU) | Processamento e hospedagem de aplicações |
| Object Storage (S3) | Armazenamento de arquivos, datasets e modelos |
| RDS (Postgres/pgvector) | Banco de dados relacional e vetorial |

## Arquitetura de exemplo

![Diagrama Nível 1](leve_1.png)

Neste diagrama, o usuário acessa um front-end estático que se comunica com uma API Flask no EC2, que por sua vez conecta ao PostgreSQL no RDS — exatamente o que construímos neste curso.

## Vantagens

- Controle total sobre a infraestrutura e o código.
- Flexibilidade máxima para escolher tecnologias e configurações.
- Custo previsível com instâncias reservadas ou Free Tier.

## Desafios

- O time é responsável por segurança, escalabilidade, backups e monitoramento.
- Maior esforço operacional para manter tudo funcionando.
- Escalar exige configuração manual (ou automação própria).

## Quando usar

Ideal para aprendizado, MVPs, projetos com requisitos muito específicos ou quando o time precisa de controle total sobre cada componente.

---

→ Próximo: [Nível 2 — Modelos e Serviços de ML](nivel_2.md)
