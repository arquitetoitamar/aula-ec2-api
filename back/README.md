# Configuração do Ambiente no EC2 (Guia rápido para a Sprint)

Este arquivo descreve instruções simples para executar o exemplo `back/api.py` localmente e em uma instância EC2 (passos mínimos para a atividade da Sprint).

Pré-requisitos
- Acesso à instância EC2 com a chave PEM (se for usar EC2).
- Python 3 instalado (ex: python3.8+).

Rodando localmente (Windows / macOS / Linux)

```bash
# criar e ativar um virtualenv
python3 -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\Activate    # Windows (PowerShell)

# instalar dependências
pip install -r requirements.txt

# rodar a API
python api.py
```

No exemplo deste repositório, o arquivo está em `back/api.py`. Se você estiver no diretório `back`, rode `python api.py`.

Testes rápidos (local)

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/echo/ola
```

Instalação mínima em EC2 (passos resumidos)

1. Conectar via SSH:

```bash
ssh -i "sua-chave.pem" ubuntu@SEU_IP_PUBLICO
```

2. Atualizar e instalar Python:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip
```

3. Criar projeto e rodar:

```bash
mkdir -p ~/app && cd ~/app
# transferir os arquivos (scp/git)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python back/api.py
```

4. Teste pela máquina local (substitua SEU_IP_PUBLICO):

```bash
curl http://SEU_IP_PUBLICO:5000/health
```

Notas para produção (opcional)
- Para produção, prefira executar a aplicação atrás de Gunicorn+Nginx ou usando systemd para manter o processo em pé.
- Ajuste o Security Group para permitir apenas os IPs necessários para SSH (porta 22) e a porta da aplicação (5000) conforme solicitado na atividade.

Comandos úteis

```bash
# ver processos
ps aux | grep api.py

# parar (se rodando em background)
kill <PID>
```

---

Este guia foi simplificado para a atividade de aprendizado; siga as seções em `docs/implementation-guide/tutorials/criar-ec2.md` para instruções passo a passo e screenshots recomendadas.