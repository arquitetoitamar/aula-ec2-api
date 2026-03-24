# Back-end — API FlexMedia

API Flask com conexão ao PostgreSQL (RDS).

## Rodar localmente

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python api.py
```

## Rodar na EC2

```bash
export DB_HOST="SEU_ENDPOINT_RDS"
export DB_PORT="5432"
export DB_NAME="postgres"
export DB_USER="postgres"
export DB_PASSWORD="SUA_SENHA"

python api.py
```

## Testes rápidos

```bash
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/items
curl -X POST http://127.0.0.1:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Teste", "description": "Item de teste"}'
```
