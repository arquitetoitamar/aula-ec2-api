# Back-end — API

API Flask com conexão ao PostgreSQL (RDS).

## Rodar localmente

```bash
sudo apt install python3.12-venv #instalar lib
python3 -m venv venv # criar ambiente virutal
source venv/bin/activate # ativa o ambiente
pip install -r requirements.txt # instala as dependencias
python api.py # executa a api
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
