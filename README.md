# TaskFlow API

API REST para gerenciamento de tarefas, desenvolvida como projeto de estudo em back-end com Python.

## Tecnologias

- **Python 3.13**
- **FastAPI** — framework web para construção da API
- **SQLAlchemy** — ORM para comunicação com o banco de dados
- **SQLite** — banco de dados
- **Pydantic** — validação de dados de entrada e saída
- **Uvicorn** — servidor ASGI

## Funcionalidades

- Cadastro e login de usuário com autenticação JWT
- Criar tarefa (`POST /tasks`)
- Listar todas as tarefas do usuário autenticado (`GET /tasks`)
- Buscar tarefa por ID (`GET /tasks/{task_id}`)
- Atualizar tarefa (`PUT /tasks/{task_id}`)
- Remover tarefa (`DELETE /tasks/{task_id}`)

## Como rodar o projeto

Clone o repositório e, na raiz do projeto, crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

Instale as dependências:

```bash
pip install fastapi uvicorn sqlalchemy
```

Suba o servidor:

```bash
uvicorn app.main:app --reload
```

A documentação interativa fica disponível em `http://127.0.0.1:8000/docs`.

## Endpoints

| Método | Rota              | Descrição                  | Status de sucesso |
|--------|-------------------|-----------------------------|--------------------|
| POST   | /tasks             | Cria uma nova tarefa        | 201 Created        |
| GET    | /tasks             | Lista todas as tarefas      | 200 OK             |
| GET    | /tasks/{task_id}   | Busca uma tarefa por ID     | 200 OK             |
| PUT    | /tasks/{task_id}   | Atualiza uma tarefa         | 200 OK             |
| DELETE | /tasks/{task_id}   | Remove uma tarefa           | 204 No Content     |

## Estrutura do projeto

```
taskflow-api/
├── app/
│ ├── main.py # Rotas e inicialização da aplicação
│ ├── models.py # Modelos SQLAlchemy (tabelas)
│ ├── schemas.py # Schemas Pydantic (validação)
│ └── database.py # Configuração da conexão com o banco
├── requirements.txt
└── README.md
```

## Próximos passos

- Testes automatizados com pytest
- Containerização com Docker