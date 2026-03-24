# Arquitetura da Aplicação

![Diagrama da Arquitetura](arquitetura.png)

## Componentes

| Componente | Tecnologia | Função |
|------------|-----------|--------|
| Front-end | Site estático (Object Storage / CDN) | Interface do usuário |
| API | Python Flask em instância EC2 | Lógica de negócio e endpoints REST |
| Banco de Dados | PostgreSQL no Amazon RDS | Persistência de dados |

## Fluxo

1. O usuário acessa o front-end estático hospedado em Object Storage ou CDN.
2. O front-end faz requisições HTTP para a API Flask rodando na instância EC2.
3. A API processa as requisições e se conecta ao PostgreSQL no RDS para ler e gravar dados.
4. A resposta retorna ao front-end em formato JSON.

## Decisões Técnicas

- **EC2 (t2.micro / t3.micro)** — elegível ao Free Tier, suficiente para aprendizado.
- **RDS PostgreSQL (db.t3.micro)** — banco gerenciado, sem necessidade de administrar o servidor de banco.
- **Flask** — micro framework leve, ideal para APIs simples e aprendizado.
- **Security Groups** — controle de acesso por portas (22 para SSH, 5000 para API, 5432 para PostgreSQL).
