# Níveis de Maturidade de Plataformas de IA na Nuvem

A evolução de uma plataforma de IA na nuvem pode ser dividida em três níveis principais de maturidade. Cada nível representa um avanço em automação, facilidade de uso, integração e potencial de inovação.

## Nível 1: Hardware e Infraestrutura

Neste estágio, a empresa utiliza recursos básicos de nuvem para construir sua própria stack de IA. Exemplos:
- Instâncias EC2 (com ou sem GPU)
- Armazenamento S3
- Banco de dados RDS (Postgres/pgvector)

**Vantagens:**
- Total controle sobre a infraestrutura
- Flexibilidade máxima

**Desafios:**
- Maior responsabilidade operacional
- Menor automação
- Escalabilidade e segurança dependem do time

Veja o diagrama: [leve_1.puml](leve_1.puml)

---

## Nível 2: Modelos e Serviços de ML Gerenciados

Neste estágio, a empresa adota serviços gerenciados de machine learning, como o Amazon SageMaker, para treinar, hospedar e operacionalizar modelos.

**Vantagens:**
- Menos preocupação com infraestrutura
- Ferramentas integradas para ML
- Escalabilidade facilitada

**Desafios:**
- Menos controle sobre detalhes de baixo nível
- Custo pode ser maior

Veja o diagrama: [leve_2.puml](leve_2.puml)

---

## Nível 3: Aplicações e Serviços de IA

O estágio mais avançado, onde a empresa utiliza serviços de IA prontos (como Amazon Bedrock, AWS AI Services, modelos fundamentais, agentes, etc.) e foca em construir aplicações inteligentes, serverless e altamente integradas.

**Vantagens:**
- Time-to-market muito rápido
- Baixa complexidade operacional
- Foco total no negócio

**Desafios:**
- Menor customização
- Dependência de provedores

Veja o diagrama: [leve_3.puml](leve_3.puml)

---

> A jornada de maturidade começa com a base de infraestrutura (nível 1), evolui para serviços gerenciados de ML (nível 2) e culmina em aplicações inteligentes e serverless (nível 3). Cada etapa traz ganhos de produtividade, automação e inovação.
