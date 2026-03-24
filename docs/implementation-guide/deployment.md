# Deploy

## Ambiente de Aprendizado

Para fins didáticos, a API roda diretamente com o servidor de desenvolvimento do Flask:

```bash
export DB_HOST="SEU_ENDPOINT_RDS"
export DB_PASSWORD="SUA_SENHA"
python app.py
```

## Dicas para Produção

Para um ambiente mais robusto, considere:

- **Gunicorn** — servidor WSGI para rodar a aplicação Flask com múltiplos workers.
- **Nginx** — proxy reverso na frente do Gunicorn para gerenciar conexões.
- **systemd** — manter a aplicação rodando como serviço do sistema operacional.
- **Variáveis de ambiente** — nunca coloque senhas diretamente no código; use variáveis de ambiente ou um gerenciador de segredos (ex: AWS Secrets Manager).
