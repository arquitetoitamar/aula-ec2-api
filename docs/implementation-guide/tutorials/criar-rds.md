# Aula 2 — Criar o Banco de Dados RDS (PostgreSQL)

🎯 **Objetivo:** Criar um banco de dados PostgreSQL gerenciado na AWS usando o Amazon RDS.

## O que é o RDS?

O Amazon RDS (Relational Database Service) é um serviço que cria e gerencia bancos de dados na nuvem. Ele cuida de backups, atualizações e manutenção para você.

## Passo a Passo

### 1. Acessar o RDS no Console

- No Console AWS, busque por **RDS** e clique no serviço.
- Clique em **Create database**.

### 2. Configurar o Banco

Preencha as opções:

| Campo | Valor |
|-------|-------|
| Creation method | Standard create |
| Engine | PostgreSQL |
| Engine version | (manter a padrão) |
| Templates | **Free tier** |
| DB instance identifier | `flexmedia-db` |
| Master username | `postgres` |
| Master password | (escolha uma senha e anote) |
| DB instance class | `db.t3.micro` |
| Storage | 20 GB (padrão) |
| Public access | **Yes** (para fins de aprendizado) |

> ⚠️ Em produção, o banco **nunca** deve ter acesso público. Para aprendizado, habilitamos para facilitar os testes.

### 3. Configurar o Security Group do RDS

Na seção de conectividade, crie ou edite o Security Group do RDS para permitir conexões na porta 5432:

| Tipo | Porta | Origem | Uso |
|------|-------|--------|-----|
| PostgreSQL | 5432 | Security Group da EC2 | Permitir que a API acesse o banco |

> 💡 A forma mais segura é permitir acesso apenas a partir do Security Group da EC2, em vez de abrir para qualquer IP.

### 4. Criar o Banco

- Clique em **Create database**.
- Aguarde alguns minutos até o status mudar para **Available**.
- Anote o **Endpoint** do banco (algo como `flexmedia-db.xxxx.us-east-1.rds.amazonaws.com`).

### 5. Testar a Conexão (opcional)

Se tiver o `psql` instalado localmente ou na EC2:

```bash
psql -h SEU_ENDPOINT_RDS -U postgres -d postgres
```

Digite a senha quando solicitado. Se conectar, o banco está pronto!

## Validação

- [ ] Instância RDS com status **Available**.
- [ ] Endpoint do banco anotado.
- [ ] Security Group permite conexão na porta 5432 a partir da EC2.

## Próximo Passo

→ [Aula 3 — Configurar ambiente Python e subir a API](configurar-ambiente.md)
