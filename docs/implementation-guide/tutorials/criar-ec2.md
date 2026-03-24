# Aula 1 — Criar a Instância EC2 na AWS

🎯 **Objetivo:** Criar uma máquina virtual (EC2) na AWS com Ubuntu, elegível ao Free Tier.

## O que é o EC2?

O Amazon EC2 (Elastic Compute Cloud) é um serviço que permite criar máquinas virtuais na nuvem. Pense nele como um computador remoto que você acessa pela internet.

## Passo a Passo

### 1. Acessar o Console AWS

- Acesse [https://aws.amazon.com/](https://aws.amazon.com/) e faça login na sua conta.
- No campo de busca, digite **EC2** e clique no serviço.

### 2. Criar a Instância

- Clique em **Launch instances**.
- Preencha:
    - **Name:** `flexmedia-api`
    - **AMI:** Ubuntu Server 22.04 LTS (Free Tier eligible)
    - **Instance type:** `t2.micro` ou `t3.micro` (Free Tier)
    - **Key pair:** clique em *Create new key pair*, dê um nome (ex: `minha-chave`), mantenha o formato `.pem` e faça o download. **Guarde este arquivo com segurança — você não poderá baixá-lo novamente.**

### 3. Configurar o Security Group

Na seção **Network settings**, clique em **Edit** e adicione as seguintes regras de entrada (Inbound rules):

| Tipo | Porta | Origem | Uso |
|------|-------|--------|-----|
| SSH | 22 | Meu IP | Acesso remoto ao servidor |
| Custom TCP | 5000 | 0.0.0.0/0 | Acesso à API Flask |

> ⚠️ Em produção, nunca deixe portas abertas para `0.0.0.0/0`. Para fins de aprendizado, é aceitável.

### 4. Lançar a Instância

- Clique em **Launch instance**.
- Aguarde o status mudar para **Running**.
- Anote o **IP Público** da instância (você vai precisar dele).

### 5. Conectar via SSH

No terminal do seu computador:

```bash
# Ajustar permissão da chave (necessário apenas na primeira vez)
chmod 400 /caminho/para/minha-chave.pem

# Conectar
ssh -i /caminho/para/minha-chave.pem ubuntu@SEU_IP_PUBLICO
```

No Windows, use Git Bash, PowerShell (com OpenSSH) ou WSL.

Se a conexão funcionar, você verá o prompt do Ubuntu. Parabéns, sua EC2 está no ar! 🎉

## Validação

- [ ] Instância EC2 com status **Running**.
- [ ] Security Group com portas 22 e 5000 abertas.
- [ ] Conexão SSH funcionando.

## Próximo Passo

→ [Aula 2 — Criar o banco de dados RDS](criar-rds.md)
