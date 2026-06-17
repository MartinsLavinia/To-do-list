# 📘 GUIA DO USUÁRIO

Este guia explica de forma simples como baixar, configurar e rodar o sistema em qualquer máquina usando Docker.

---

## 📌 Pré-requisitos

Antes de começar, você precisa ter instalado:

- Git
- Docker
- Docker Compose
- Navegador (Chrome, Firefox, etc.)

👉 Se estiver no Windows, recomenda-se usar **Docker Desktop**.

---

## 📥 Como baixar o projeto

Abra o terminal e execute:

```
git clone https://github.com/MartinsLavinia/To-do-list.git
```

Depois entre na pasta do projeto:
```
cd To-do-list
```
## 🔐 Como configurar o arquivo .env

Na raiz do projeto, crie um arquivo chamado .env:
```
DB_HOST=db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

💡 Esse arquivo é essencial para o sistema se conectar ao banco de dados.

## 🐳 Como subir os containers

Dentro da pasta do projeto, execute:

```
docker compose up --build
```

Esse comando vai:

Criar os containers
Subir o banco de dados MySQL
Rodar a aplicação Flask

Se quiser rodar em segundo plano:

```
docker compose up -d
```
## 🌐 Como acessar pelo navegador

Depois que os containers estiverem rodando, abra o navegador e acesse:

💻 Localmente:
http://localhost:5000
☁️ Servidor (AWS EC2):
http://50.19.141.64:5000
⛔ Como parar o sistema

Para desligar tudo corretamente, use:
```
docker compose down
```

Isso irá:

Parar os containers
Liberar os recursos da máquina