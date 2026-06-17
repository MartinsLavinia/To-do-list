# 🚀 Sistema Web com Flask + MySQL (Docker + AWS EC2)

## 📌 Nome do Projeto
Sistema Web de Gerenciamento com Flask e MySQL

---

## 📖 Descrição do Sistema

Este projeto é uma aplicação web desenvolvida com **Flask (Python)** no backend e **MySQL** como banco de dados relacional.

O sistema permite realizar operações básicas de cadastro e gerenciamento de dados, com persistência em banco e comunicação entre serviços via rede Docker.

Toda a aplicação foi containerizada com **Docker** e orquestrada com **Docker Compose**, permitindo execução simples tanto em ambiente local quanto em produção (AWS EC2).

---

## 🧠 Tecnologias Utilizadas

### 🔙 Backend
- Python
- Flask
- MySQL
- mysql-connector-python
- python-dotenv

### 🐳 DevOps / Infraestrutura
- Docker
- Docker Compose
- Docker Hub
- AWS EC2
- Git / GitHub

---

## ⚙️ Funcionalidades

- Integração entre Flask e MySQL
- CRUD básico (criação, leitura, atualização e remoção de dados)
- Persistência de dados em banco relacional
- Configuração via variáveis de ambiente (.env)
- Execução via Docker e Docker Compose
- Deploy em instância AWS EC2
- Separação de serviços em containers (web + database)

---

## 📁 Estrutura de Pastas

```text
projeto/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── script.sql
│
├── static/
│   └── style.css
│
├── templates/
│   └── HTMLs do sistema
│
└── README.md
```

---

## 🛠️ Como Instalar o Projeto

### 1️⃣ Clonar o repositório
```
git clone [https://github.com/MartinsLavinia/To-do-list.git](https://github.com/MartinsLavinia/To-do-list.git)
```
### 2️⃣ Acessar a pasta do projeto
```
cd To-do-list
```
### 3️⃣ Instalar dependências (caso rode local sem Docker)
```
pip install -r requirements.txt
```

## 🔐 Configuração do arquivo .env
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

```
DB_HOST=db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

---

## 🐳 Como Rodar com Docker
### 🔨 Build e execução dos containers
```
docker compose up --build
```
### ▶️ Rodar em segundo plano
```
docker compose up -d
```
### ⛔ Parar os containers
```
docker compose down
```

---

## 🌐 Como Acessar o Sistema
💻 Localmente: http://localhost:5000

☁️ AWS EC2: http://50.19.141.64:5000

## 🐳 Docker Hub
Imagem do projeto disponível em:
👉 Repositório no Docker Hub

## ☁️ Deploy na AWS EC2
A aplicação foi implantada em uma instância AWS EC2, utilizando Docker e Docker Compose.
Os serviços são separados em containers independentes:

Flask (aplicação web)

MySQL (banco de dados)

Isso garante:

Portabilidade

Facilidade de deploy

Escala básica

Isolamento de serviços

---

## 👨‍💻 Autor
Lavinia Martins - Projeto desenvolvido para fins acadêmicos utilizando Flask, MySQL, Docker, Docker Compose, Docker Hub e AWS EC2.