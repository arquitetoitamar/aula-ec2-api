# API FlexMedia

Documentação completa: [https://arquitetoitamar.github.io/aula-ec2-api/](https://arquitetoitamar.github.io/aula-ec2-api/)

## Visão Geral

API RESTful em Flask que conecta a um banco PostgreSQL (RDS). Projeto didático para aprender a implantar aplicações Python na nuvem AWS.

## Arquitetura

- **Front-end** → Site estático (Object Storage / CDN)
- **API** → Python Flask em instância EC2
- **Banco de Dados** → PostgreSQL no Amazon RDS

## Conteúdo Programático

1. [Criar a instância EC2](docs/implementation-guide/tutorials/criar-ec2.md) — Ubuntu Free Tier na AWS
2. [Criar o banco RDS](docs/implementation-guide/tutorials/criar-rds.md) — PostgreSQL gerenciado
3. [Configurar ambiente e subir a API](docs/implementation-guide/tutorials/configurar-ambiente.md) — Python, Flask, API inicial
4. [Integrar API com banco](docs/implementation-guide/tutorials/integrar-api-banco.md) — Conexão com PostgreSQL e rotas CRUD

## Como rodar localmente

```bash
cd back
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python api.py
```

Teste:

```bash
curl http://127.0.0.1:5000/health
```

## API — Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Mensagem de boas-vindas |
| GET | `/health` | Health check |
| GET | `/items` | Listar itens |
| POST | `/items` | Criar item |
| GET | `/items/<id>` | Buscar item por ID |
| PUT | `/items/<id>` | Atualizar item |
| DELETE | `/items/<id>` | Remover item |
