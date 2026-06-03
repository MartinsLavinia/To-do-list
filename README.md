# 📝 Bloco de Notas

Um sistema simples de gerenciamento de notas desenvolvido com Flask, MySQL, HTML, CSS e Bootstrap.

O objetivo do projeto é permitir que o usuário crie, visualize, edite e exclua notas de forma rápida e intuitiva através de uma interface limpa e responsiva.

---

## 📸 Funcionalidades

- ✅ Criar novas notas
- ✅ Visualizar todas as notas cadastradas
- ✅ Editar notas existentes
- ✅ Excluir notas
- ✅ Confirmação antes da exclusão
- ✅ Mensagens de sucesso para operações realizadas
- ✅ Interface responsiva
- ✅ Integração com banco de dados MySQL

---

## 🛠️ Tecnologias Utilizadas

### Backend
- Python
- Flask
- MySQL
- mysql-connector-python

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons

---

## 📂 Estrutura do Projeto

```text
To-do-list/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── nova_nota.html
│   └── editar_nota.html
│
├── app.py
├── conexao.py
├── README.md
│
└── __pycache__/
```

---

## 🗄️ Estrutura da Tabela

| Campo | Tipo | Descrição |
|---------|---------|---------|
| not_id | INT | Identificador da nota |
| not_titulo | VARCHAR(255) | Título da nota |
| not_conteudo | TEXT | Conteúdo da nota |
| not_data_criacao | TIMESTAMP | Data e hora de criação da nota |

---

## 🎨 Interface

O sistema possui:

- Tema escuro
- Cards para exibição das notas
- Botão flutuante para criação de notas
- Ícones para edição e exclusão
- Modal de confirmação para exclusão
- Mensagens de feedback para o usuário

---

## 🔄 Operações CRUD

### Create
Criação de novas notas.

### Read
Listagem de todas as notas cadastradas.

### Update
Edição de notas existentes.

### Delete
Remoção de notas com confirmação prévia.

---

## 👩‍💻 Autora

Desenvolvido por Lavinia como projeto de estudo para prática de:

- Flask
- CRUD
- MySQL
- HTML e CSS
- Bootstrap
- Integração Frontend + Backend

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado.