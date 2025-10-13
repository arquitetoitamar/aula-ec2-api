# Como criar uma instância EC2 Ubuntu na Free Tier da AWS

> Este tutorial mostra como criar uma instância EC2 Ubuntu elegível para o nível gratuito (free tier) da AWS, ideal para testes e aprendizado.

## 1. Acesse o Console AWS
- Entre em https://aws.amazon.com/ e faça login na sua conta.

## 2. Acesse o serviço EC2
- No menu "Services", procure por **EC2** e clique para abrir o painel.

## 3. Clique em "Launch Instance"
- Clique no botão **Launch Instance**.

## 4. Configure os detalhes da instância
- **Name**: Dê um nome para sua instância (ex: `ubuntu-teste`).
- **Application and OS Images (AMI)**: Selecione **Ubuntu Server 22.04 LTS (HVM), SSD Volume Type** (ou versão mais recente elegível para free tier).
- **Instance type**: Selecione **t2.micro** (Free tier eligible).
- **Key pair (login)**: Crie um novo par de chaves ou selecione um existente. Baixe e guarde o arquivo `.pem` com segurança.
- **Network settings**: Permita SSH (porta 22) e, se for rodar uma API, HTTP (porta 80) e/ou HTTPS (porta 443).
- **Storage**: O padrão (8 GB) já é suficiente para testes.

## 5. Clique em "Launch Instance"
- Revise as configurações e clique em **Launch Instance**.

## 6. Acesse sua instância via SSH
- No painel do EC2, selecione sua instância e clique em **Connect**.
- Siga as instruções para conectar via SSH. Exemplo de comando:

```bash
ssh -i /caminho/para/sua-chave.pem ubuntu@<ENDERECO_PUBLICO_DA_EC2>
```

> Dica: No Windows, use o Git Bash ou WSL para rodar o comando SSH.

## 7. (Opcional) Instale pacotes básicos
Após conectar, atualize o sistema e instale utilitários:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3-pip -y
```

Pronto! Sua instância EC2 Ubuntu está pronta para uso na free tier da AWS.