# Considerações

## Segurança

- Nunca exponha o banco de dados (RDS) com acesso público em produção.
- Restrinja o Security Group da EC2 para aceitar SSH apenas do seu IP.
- Use variáveis de ambiente para credenciais — nunca coloque senhas no código-fonte.
- Proteja o arquivo `.pem` da chave SSH (permissão `400`).

## Disponibilidade

- O servidor de desenvolvimento do Flask não é adequado para produção. Use Gunicorn + Nginx.
- Considere usar um Elastic IP para manter o IP público fixo na EC2.

## Banco de Dados

- Habilite backups automáticos no RDS.
- Use conexões com pool em aplicações com maior volume de requisições.
