# Bloco de Notas Web

## Descrição do Projeto

O Bloco de Notas Web é uma aplicação desenvolvida para permitir o gerenciamento de anotações de forma simples e intuitiva. O sistema possibilita criar, visualizar, editar e excluir notas armazenadas em um banco de dados MySQL.

O projeto foi desenvolvido utilizando Python com Flask no back-end e HTML, CSS e Bootstrap no front-end.

---

## Tecnologias Utilizadas

### Back-end

* Python
* Flask
* MySQL
* mysql-connector-python
* python-dotenv

### Front-end

* HTML5
* CSS3
* Bootstrap 5

### DevOps

* Docker
* Docker Compose
* Docker Hub
* AWS EC2

---

## Funcionalidades

* Criar notas
* Visualizar notas cadastradas
* Editar notas existentes
* Excluir notas
* Persistência de dados em banco MySQL
* Configuração por variáveis de ambiente (.env)
* Execução via Docker e Docker Compose

---

## Estrutura de Pastas

```text
bloco_notas/
│
├── app.py
├── dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── script.sql
│
├── static/
│   └── style.css
│
├── templates/
│
└── README.md
```

---

## Como Instalar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/SEU_USUARIO/bloco_notas.git
```

### 2. Entrar na Pasta do Projeto

```bash
cd bloco_notas
```

### 3. Criar um Ambiente Virtual

```bash
python -m venv venv
```

### 4. Ativar o Ambiente Virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux

```bash
source venv/bin/activate
```

### 5. Instalar as Dependências

```bash
pip install -r requirements.txt
```

---

## Configuração do Arquivo .env

Crie um arquivo chamado `.env` na raiz do projeto contendo:

```env
DB_HOST=db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=bloco_notas
```

---

## Executando o Projeto sem Docker

Execute:

```bash
python app.py
```

Acesse:

```text
http://localhost:5000
```

---

## Executando com Docker

### Construir a Imagem

```bash
docker build -t bloco_notas .
```

### Iniciar os Containers

```bash
docker compose up --build
```

### Executar em Segundo Plano

```bash
docker compose up -d
```

### Parar os Containers

```bash
docker compose down
```

---

## Banco de Dados

O banco de dados utilizado é o MySQL.

A estrutura e os dados iniciais encontram-se no arquivo:

```text
script.sql
```

Esse arquivo é executado automaticamente durante a inicialização do container MySQL.

---

## Como Acessar o Sistema

Após iniciar os containers:

```text
http://localhost:5000
```

Caso esteja hospedado na AWS EC2:

```text
http://IP_PUBLICO_DA_INSTANCIA:5000
```

---

## Docker Hub

Imagem publicada no Docker Hub:

```text
https://hub.docker.com/r/SEU_USUARIO/bloco_notas
```

(Substituir pelo link real após a publicação.)

---

## AWS EC2

A aplicação foi implantada em uma instância AWS EC2 utilizando Docker e Docker Compose.

A infraestrutura permite a execução da aplicação e do banco de dados em containers independentes, garantindo portabilidade e facilidade de implantação.

---

## Prints das Telas

### Tela Inicial

Inserir print da tela inicial.

### Tela de Criação de Nota

Inserir print da tela de criação de nota.

### Tela de Edição de Nota

Inserir print da tela de edição de nota.

### Aplicação Rodando na AWS EC2

Inserir print da aplicação em execução na instância EC2.

### Containers Ativos

Inserir print do comando:

```bash
docker ps
```

### Imagem Publicada no Docker Hub

Inserir print da imagem publicada no Docker Hub.

---

## Autor

Lavinia

Projeto desenvolvido para fins acadêmicos utilizando Flask, MySQL, Docker, Docker Compose, Docker Hub e AWS EC2.
