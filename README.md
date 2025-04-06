# Atividade Engenharia de Software
# 🎓 Sistema de Cadastro de Alunos (Python/Flask)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.x-lightgrey)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-green)](https://www.sqlite.org/)

Um sistema web completo para gerenciamento de alunos de faculdade, com cadastro, edição, exclusão e exportação de dados.

## ✨ Funcionalidades

- ✅ **CRUD completo** (Create, Read, Update, Delete)
- 🔍 Busca por nome, CPF ou matrícula
- 📁 Exportação para JSON
- 📱 Responsivo (com Bootstrap 5)
- 🛡️ Validação de CPF/matrícula únicos

## 🛠️ Tecnologias

- **Backend**: Python + Flask
- **Frontend**: HTML5 + Bootstrap 5
- **Banco de Dados**: SQLite (suporta MySQL com 1 alteração)
- **ORM**: SQLAlchemy

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/cadastro-alunos.git
   cd cadastro-alunos
   
2. Instale as dependências:
    ```bash
   pip install -r requirements.txt
   
4. Execute a aplicação:
    ```bash
   python app.py

6. Acesse no navegador:
    ```bash
   http://localhost:5000

📦 Estrutura do Projeto
 ```bash
cadastro-alunos/
├── app.py                # Aplicação principal
├── models.py             # Modelos do banco de dados
├── requirements.txt      # Dependências
├── alunos.db             # Banco de dados SQLite (gerado automaticamente)
├── static/               # CSS/JS se tiver
└── templates/            # Páginas HTML
    ├── base.html         # Layout principal
    ├── index.html        # Listagem de alunos
    ├── cadastro.html     # Formulário de cadastro
    ├── editar.html       # Edição de registros
    └── buscar.html       # Resultados de busca

```
📌 Exemplo de Uso
Cadastrar novo aluno:

Acesse /cadastrar

Preencha os dados (CPF e matrícula são únicos)

Exportar dados:

Clique em "Exportar como JSON" para baixar todos os registros

Buscar alunos:

Digite qualquer termo na barra de pesquisa
