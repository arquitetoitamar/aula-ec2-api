# Back-end — API Flask

API REST em Python/Flask com conexão ao PostgreSQL (AWS RDS).

## Por que fazer deploy de uma API na nuvem?

Saber colocar uma API em produção na nuvem é uma competência central para quem trabalha — ou quer trabalhar — com **Inteligência Artificial e Cloud Computing**. Os motivos vão além da infraestrutura: eles moldam como sistemas de IA são construídos e consumidos no mundo real.

### APIs são a interface dos sistemas de IA

Modelos de linguagem (LLMs), visão computacional, recomendação e outros serviços de IA são entregues **via API HTTP**. A OpenAI, a Anthropic, o Google Gemini e a AWS Bedrock expõem seus modelos exatamente assim — um endpoint REST que recebe uma requisição e devolve uma resposta. Entender como uma API funciona por dentro é o primeiro passo para integrar e construir em cima desses serviços.

### Escalabilidade e disponibilidade

Uma aplicação rodando só no laptop é um protótipo. Uma API na nuvem pode:

- **Escalar horizontalmente** — múltiplas instâncias EC2 ou containers atendendo milhares de requisições simultâneas;
- **Ficar disponível 24/7** — monitoramento, restart automático e multi-região garantem que o modelo responda mesmo durante falhas;
- **Integrar com bancos gerenciados** — como o AWS RDS, que cuida de backups, patches e alta disponibilidade do PostgreSQL sem trabalho manual.

### Banco de dados é memória de longo prazo para IA

Modelos de IA não têm memória persistente por padrão. O banco de dados conectado à API é quem armazena:

- histórico de conversas e sessões de usuários;
- embeddings e vetores para busca semântica (RAG — Retrieval-Augmented Generation);
- logs de uso, métricas de qualidade e feedback para fine-tuning.

Nesta aula, a tabela `usuarios` é simples de propósito — o objetivo é solidificar o pipeline **EC2 → Flask → RDS** antes de evoluir para casos de uso com IA.

### Cloud é o ambiente natural do ciclo de vida de IA

| Etapa do ciclo de IA            | Serviço AWS envolvido     |
| ------------------------------- | -------------------------- |
| Coleta e armazenamento de dados | S3, RDS, DynamoDB          |
| Treinamento e fine-tuning       | EC2 (GPU), SageMaker       |
| Inferência / serving do modelo | EC2, ECS, Lambda, Bedrock  |
| Exposição via API             | API Gateway, ALB + EC2/ECS |
| Monitoramento e observabilidade | CloudWatch, X-Ray          |

Fazer o deploy desta API Flask na EC2 conectada ao RDS coloca você no mesmo fluxo que equipes de engenharia de ML e MLOps usam em produção — só que em escala menor, ideal para aprender os fundamentos sem ruído.

---

## Pré-requisitos

- Python 3.12+
- Acesso a uma instância PostgreSQL (local ou RDS)

## Dependências

| Pacote          | Versão |
| --------------- | ------- |
| Flask           | 3.0.0   |
| psycopg2-binary | 2.9.9   |
| gunicorn        | 21.2.0  |

## Configuração do banco de dados

As credenciais estão definidas diretamente em `api.py` no dicionário `DB_CONFIG`. Antes de subir em produção, ajuste o host e a senha:

```python
DB_CONFIG = {
    'host': 'SEU_ENDPOINT_RDS',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'SUA_SENHA',
    'port': 5432
}
```

A tabela esperada no banco:

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL
);
```

## Rodar localmente

```bash
sudo apt install python3.12-venv          # instalar suporte a venv
python3 -m venv venv                      # criar ambiente virtual
source venv/bin/activate                  # ativar o ambiente
pip install -r requirements.txt           # instalar dependências
python api.py                             # iniciar a API na porta 3000
```

## Rodar na EC2

```bash
# Clonar e instalar
git clone https://github.com/arquitetoitamar/aula-ec2-api.git
cd aula-ec2-api/back
sudo apt install python3.12-venv #instalar lib
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python python api.py

# Editar DB_CONFIG em api.py com as credenciais do RDS
python api.py
```

Para manter a API rodando após fechar o terminal:

```bash
nohup python api.py > api.log 2>&1 &
```

## Rodar com Gunicorn (produção)

O Gunicorn é um servidor WSGI adequado para produção — substitui o servidor de desenvolvimento do Flask.

### Gunicorn rodando como processo

```bash
nohup /home/ubuntu/aula-ec2-api/back/venv/bin/gunicorn --workers 2 --bind 0.0.0.0:3000 api:app
```

### Configurar como serviço systemd (OPCIONAL)

Crie o arquivo de serviço:

```bash
sudo nano /etc/systemd/system/api.service
```

Conteúdo do arquivo (ajuste o caminho conforme sua instalação):

```ini
[Unit]
Description=API Flask — Aula Cloud AWS
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/aula-ec2-api/back
ExecStart=/home/ubuntu/aula-ec2-api/back/venv/bin/gunicorn \
    --workers 2 \
    --bind 0.0.0.0:3000 \
    --access-logfile /var/log/api/access.log \
    --error-logfile /var/log/api/error.log \
    api:app
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Crie o diretório de logs e ative o serviço:

```bash
sudo mkdir -p /var/log/api
sudo chown ubuntu:ubuntu /var/log/api

sudo systemctl daemon-reload        # recarrega configurações do systemd
sudo systemctl enable api           # habilita início automático no boot
sudo systemctl start api            # inicia o serviço agora
```

### Comandos úteis

```bash
sudo systemctl status api           # verificar status
sudo systemctl restart api          # reiniciar após mudanças no código
sudo systemctl stop api             # parar o serviço
sudo journalctl -u api -f           # acompanhar logs em tempo real
```

## Rotas disponíveis

### `GET /`

Mensagem de boas-vindas.

```bash
curl http://127.0.0.1:3000/
```

```json
{ "message": "Bem-vindo à API!" }
```

---

### `GET /health`

Verifica o status do serviço.

```bash
curl http://127.0.0.1:3000/health
```

```json
{ "service": "AULA CLOUD AWS", "status": "ok", "version": "1.0.0" }
```

---

### `GET /echo/<texto>`

Retorna o texto enviado na URL.

```bash
curl http://127.0.0.1:3000/echo/ola-mundo
```

```json
{ "echo": "ola-mundo" }
```

---

### `GET /usuarios`

Lista os usuários cadastrados no PostgreSQL.

```bash
curl http://127.0.0.1:3000/usuarios
```

```json
{
  "usuarios": [
    { "id": 1, "username": "alice" },
    { "id": 2, "username": "bob" }
  ]
}
```

Em caso de erro de conexão com o banco:

```json
{ "error": "could not connect to server: Connection refused" }
```
