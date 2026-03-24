# Aula 4 — Integrar a API com o Banco de Dados

🎯 **Objetivo:** Conectar a API Flask ao PostgreSQL no RDS e criar rotas CRUD.

## Passo a Passo

### 1. Conectar na EC2 e ativar o ambiente

```bash
ssh -i /caminho/para/minha-chave.pem ubuntu@SEU_IP_PUBLICO
cd ~/app
source venv/bin/activate
```

### 2. Instalar a biblioteca de conexão com PostgreSQL

```bash
sudo apt install -y libpq-dev
pip install psycopg2-binary
```

### 3. Atualizar a API

Edite o arquivo `app.py` (ou crie um novo):

```bash
nano app.py
```

Substitua o conteúdo por:

```python
import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432"),
        dbname=os.environ.get("DB_NAME", "postgres"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", ""),
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    return jsonify(message="Bem-vindo à API FlexMedia!")

@app.route("/health")
def health():
    return jsonify(status="ok", service="flexmedia", version="1.0.0")

@app.route("/items", methods=["GET"])
def list_items():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM items")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "description": r[2]} for r in rows])

@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id",
        (data["name"], data.get("description", "")),
    )
    item_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(id=item_id, name=data["name"], description=data.get("description", "")), 201

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM items WHERE id = %s", (item_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return jsonify(error="Item não encontrado"), 404
    return jsonify(id=row[0], name=row[1], description=row[2])

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET name = %s, description = %s WHERE id = %s",
        (data["name"], data.get("description", ""), item_id),
    )
    conn.commit()
    updated = cur.rowcount
    cur.close()
    conn.close()
    if not updated:
        return jsonify(error="Item não encontrado"), 404
    return jsonify(id=item_id, name=data["name"], description=data.get("description", ""))

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    deleted = cur.rowcount
    cur.close()
    conn.close()
    if not deleted:
        return jsonify(error="Item não encontrado"), 404
    return jsonify(message="Item removido")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
```

### 4. Configurar as variáveis de ambiente e rodar

```bash
export DB_HOST="SEU_ENDPOINT_RDS"
export DB_PORT="5432"
export DB_NAME="postgres"
export DB_USER="postgres"
export DB_PASSWORD="SUA_SENHA"

python app.py
```

### 5. Testar as rotas CRUD

No seu computador local:

```bash
# Criar um item
curl -X POST http://SEU_IP_PUBLICO:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Notebook", "description": "Notebook Dell 16GB"}'

# Listar todos os itens
curl http://SEU_IP_PUBLICO:5000/items

# Buscar um item por ID
curl http://SEU_IP_PUBLICO:5000/items/1

# Atualizar um item
curl -X PUT http://SEU_IP_PUBLICO:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Notebook", "description": "Notebook Dell 32GB"}'

# Deletar um item
curl -X DELETE http://SEU_IP_PUBLICO:5000/items/1
```

## Validação

- [ ] API conectando no PostgreSQL do RDS.
- [ ] Rota `POST /items` criando registros no banco.
- [ ] Rota `GET /items` listando registros do banco.
- [ ] Rotas `PUT` e `DELETE` funcionando corretamente.

## Parabéns! 🎉

Você completou todas as aulas e tem uma aplicação completa rodando na nuvem: API Flask no EC2 conectada a um banco PostgreSQL no RDS.
