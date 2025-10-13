# Documentação

https://arquitetoitamar.github.io/aula-2-api/

# Guia de Implementação da API

Bem-vindo ao guia de implementação da sua API! Aqui você encontrará informações essenciais para entender, implantar e integrar a solução baseada neste repositório.

# Visão Geral

Este repositório contém um exemplo mínimo de API em Flask localizado em `back/api.py` e material de apoio para aprender a implantar aplicações Python na nuvem.

## Sprint: Change – FlexMedia

Tema: Criando sua primeira API Python na nuvem com AWS EC2

🎯 Objetivo da Sprint

Nesta sprint, você vai criar uma instância EC2 na AWS e subir uma aplicação simples em Python usando o Flask. A ideia é entender como colocar um programa no ar em um servidor na nuvem.

🚀 O que você vai aprender

- O que é uma instância EC2 (máquina virtual na AWS).
- Como acessar sua EC2 via SSH.
- Como instalar Python e Flask.
- Como rodar uma API e acessar pelo navegador ou terminal.
- Como publicar seu serviço e testar o acesso via internet.

🧩 Passos resumidos

1. Criar a instância EC2 (Ubuntu ou Amazon Linux) — selecionar tipo elegível ao Free Tier (t2.micro/t3.micro) e criar/baixar a chave `.pem`.
2. Abrir portas no Security Group: 22 (SSH) e 5000 (API Flask).
3. Conectar via SSH e instalar Python + pip.
4. Criar um arquivo `app.py` (ou usar `back/api.py`) e instalar Flask (`pip install -r back/requirements.txt`).
5. Rodar a API: `python back/api.py` (ou `python app.py`) e acessar `http://IP_PUBLICO:5000/health`.

Para o passo a passo completo veja: `docs/implementation-guide/tutorials/criar-ec2.md`

## Exemplo de API (back/api.py)

O arquivo `back/api.py` contém uma API mínima com as seguintes rotas:

- `/` → mensagem de boas-vindas
- `/health` → retorno JSON com status
- `/echo/<texto>` → repete o texto enviado na URL

## Como rodar localmente

1. Crie um virtualenv: `python -m venv venv` e ative-o.
2. Instale as dependências: `pip install -r back/requirements.txt`.
3. Rode a API: `python back/api.py`.
4. Teste com curl: `curl http://127.0.0.1:5000/health`.

---

Leia `docs/implementation-guide/tutorials/criar-ec2.md` para a versão completa do tutorial com comandos e capturas de tela sugeridas.
# Documentação

https://arquitetoitamar.github.io/aula-2-api/
# Guia de Implementação da API  
Bem-vindo ao guia de implementação da sua API! Aqui você encontrará informações essenciais para entender, implantar e integrar a solução baseada neste repositório.
# Visão Geral
Este projeto fornece uma API RESTful desenvolvida em Flask, que interage com um banco de dados PostgreSQL. A API é projetada para ser simples, escalável e fácil de integrar com outras aplicações.
## Componentes Principais
- **Flask**: Um micro framework web em Python, utilizado para construir a API.
- **PostgreSQL**: Um sistema de gerenciamento de banco de dados relacional, utilizado para armazenar os dados da aplicação.
