# Architecture Overview


![Diagrama da Arquitetura](arquitetura.png)

**Descrição:**

1. O usuário acessa o conteúdo estático hospedado em um armazenamento de objetos ou CDN.
2. O site faz requisições HTTP para a API desenvolvida em Flask, que está rodando em uma instância EC2.
3. A API Flask se conecta ao banco de dados PostgreSQL hospedado no Amazon RDS para armazenar e recuperar dados.

**Descrição (alternativa):**

1. O usuário acessa o conteúdo estático hospedado em um armazenamento de objetos ou CDN.
2. O site faz requisições HTTP para a API desenvolvida em Flask, que está rodando em uma instância EC2.
3. A API Flask se conecta ao banco de dados PostgreSQL hospedado no Amazon RDS para armazenar e recuperar dados.
