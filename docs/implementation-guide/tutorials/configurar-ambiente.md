# Aula 3 — Configurar Ambiente Python e Subir a API

🎯 **Objetivo:** Instalar Python e Flask na EC2 e rodar a API inicial.

## Passo a Passo

### 1. Conectar na EC2

```bash
ssh -i /caminho/para/minha-chave.pem ubuntu@SEU_IP_PUBLICO
```

### 2. Instalar Python e Dependências

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip
```

### 3. Criar o Projeto

```bash
mkdir -p ~/app && cd ~/app

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Flask

```bash
pip install Flask==3.0.0
```

### 5. Criar a API

Crie o arquivo `app.py`:

```bash
nano app.py
```

Cole o conteúdo (ou copie `back/api.py` do repositório):

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Bem-vindo à API FlexMedia!")

@app.route("/health")
def health():
    return jsonify(status="ok", service="flexmedia", version="1.0.0")

@app.route("/echo/<texto>")
def echo(texto):
    return jsonify(echo=texto)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 6. Rodar a API

```bash
python app.py
```

### 7. Testar

No seu computador local (não na EC2), abra outro terminal:

```bash
curl http://SEU_IP_PUBLICO:5000/health
curl http://SEU_IP_PUBLICO:5000/echo/ola
```

Ou acesse `http://SEU_IP_PUBLICO:5000/health` no navegador.

Você deve ver:

```json
{"status": "ok", "service": "flexmedia", "version": "1.0.0"}
```

## Validação

- [ ] API rodando na EC2 na porta 5000.
- [ ] Rota `/health` retornando JSON com status `ok`.
- [ ] Rota `/echo/teste` retornando o texto enviado.

## Próximo Passo

→ [Aula 4 — Integrar a API com o banco de dados](integrar-api-banco.md)
