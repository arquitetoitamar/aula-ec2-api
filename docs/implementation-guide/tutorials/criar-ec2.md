# Sprint: Change – FlexMedia — Criando sua primeira API Python na nuvem com AWS EC2

🎯 Objetivo da Sprint

Nesta sprint, você vai criar uma instância EC2 na AWS e subir uma aplicação simples em Python usando o Flask. A ideia é entender como colocar um programa no ar em um servidor na nuvem.

## O que você vai aprender

- O que é uma instância EC2 (máquina virtual na AWS).
- Como acessar sua EC2 via SSH.
- Como instalar Python e Flask.
- Como rodar uma API e acessar pelo navegador ou terminal.
- Como publicar seu serviço e testar o acesso via internet.

## Pré-requisitos

- Conta ativa na AWS com permissões para criar instâncias EC2 e Security Groups.
- Chave de acesso SSH (será criada no processo de Launch Instance).

## Passos da Atividade

1. Criar a instância EC2

- Acesse o Console AWS (https://aws.amazon.com/) e faça login.
- Vá para EC2 → Instances → Launch instances.
- Escolha uma AMI: Ubuntu Server 22.04 LTS (ou Amazon Linux 2).
- Instance type: selecione t2.micro ou t3.micro (Free Tier).
- Key pair: crie um novo par de chaves e baixe o arquivo `.pem`.
- Security Group: adicione regras de entrada para as portas:
	- 22 — SSH — Fonte: seu IP (recomendado) ou 0.0.0.0/0 para testes (menos seguro)
	- 5000 — TCP — Fonte: 0.0.0.0/0 (para acessar a API Flask)

2. Acessar sua EC2

- No Windows: use Git Bash, PowerShell (com OpenSSH) ou WSL para rodar ssh.
- Conectar (exemplo para Ubuntu):

```bash
ssh -i /caminho/para/sua-chave.pem ubuntu@SEU_IP_PUBLICO
```

3. Preparar o ambiente e instalar Python/Flask

```bash
# Atualizar o sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python e venv
sudo apt install -y python3 python3-venv python3-pip

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar Flask
pip install Flask==3.0.0
```

4. Criar a aplicação em Python

No diretório do projeto, crie um arquivo `app.py` (ou copie `back/api.py` do repositório). Exemplo mínimo:

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

5. Executar a aplicação

```bash
# Ative o virtualenv (se não estiver ativo)
source venv/bin/activate

# Rode a aplicação
python app.py
```

Agora a API estará disponível na porta 5000. No seu navegador ou terminal acesse:

http://SEU_IP_PUBLICO:5000/health

Você deve ver um JSON com status "ok".

6. Testar e validar

- Teste pelo navegador: acesse a rota `/health`.
- Teste pelo terminal:

```bash
curl http://SEU_IP_PUBLICO:5000/health
curl http://SEU_IP_PUBLICO:5000/echo/teste
```

- Tire prints mostrando:
	- A instância EC2 em execução.
	- As regras do Security Group (portas 22 e 5000 abertas).
	- A API funcionando no navegador ou terminal.

7. Entrega

Envie um pequeno relatório com:

- IP público da sua EC2.
- As três imagens (prints) requisitadas.
- Uma breve descrição do que foi feito em cada passo.

## Dicas

- Em produção, coloque a aplicação atrás de um servidor WSGI (Gunicorn) e um proxy reverso (Nginx). Para a atividade escolar, o servidor de desenvolvimento do Flask é suficiente.
- Lembre-se de proteger a chave `.pem` e restringir o Security Group para seu IP quando possível.

---

Arquivo de referência local: `back/api.py` (exemplo mínimo incluído no repositório).
