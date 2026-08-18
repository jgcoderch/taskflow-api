# TaskFlow API

![Tests](https://github.com/jgcoderch/taskflow-api/actions/workflows/tests.yml/badge.svg)

API REST para gerenciamento de tarefas, desenvolvida como projeto de estudo em back-end com Python. Cada usuário se cadastra, autentica via JWT, e só tem acesso às próprias tarefas.

## API em produção

🔗 [https://taskflow-api-y395.onrender.com/docs](https://taskflow-api-y395.onrender.com/docs)

## Tecnologias

- **Python 3.13**
- **FastAPI** — framework web para construção da API
- **SQLAlchemy** — ORM para comunicação com o banco de dados
- **Alembic** — versionamento e migração do esquema do banco
- **PostgreSQL** — banco de dados relacional
- **Pydantic** — validação de dados de entrada e saída
- **JWT (python-jose) + Passlib/bcrypt** — autenticação e hash de senha
- **Pytest** — testes automatizados
- **Docker + Docker Compose** — containerização da API e do banco
- **GitHub Actions** — pipeline de CI, rodando os testes a cada push
- **Render** — hospedagem em produção

## Funcionalidades

- Cadastro e login de usuário com autenticação JWT
- Criar tarefa (`POST /tasks`)
- Listar as tarefas do usuário autenticado (`GET /tasks`)
- Buscar tarefa por ID (`GET /tasks/{task_id}`)
- Atualizar tarefa (`PUT /tasks/{task_id}`)
- Remover tarefa (`DELETE /tasks/{task_id}`)
- Isolamento total de dados entre usuários

## Como rodar o projeto

### Opção 1 — Com Docker Compose (recomendado)

Sobe a API e o banco PostgreSQL juntos, já com as migrações aplicadas:

```bash
docker compose up --build -d
docker compose exec api alembic upgrade head
```

A documentação interativa fica em `http://localhost:8000/docs`.

### Opção 2 — Localmente, sem Docker

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

Nesse modo, usa SQLite por padrão (não precisa de PostgreSQL rodando).

## Rodando os testes

```bash
pytest
```

## Endpoints

| Método | Rota              | Descrição                  | Status de sucesso |
|--------|-------------------|-----------------------------|--------------------|
| POST   | /register          | Cadastra um novo usuário    | 201 Created        |
| POST   | /login              | Autentica e retorna um token JWT | 200 OK        |
| POST   | /tasks             | Cria uma nova tarefa        | 201 Created        |
| GET    | /tasks             | Lista as tarefas do usuário | 200 OK             |
| GET    | /tasks/{task_id}   | Busca uma tarefa por ID     | 200 OK             |
| PUT    | /tasks/{task_id}   | Atualiza uma tarefa         | 200 OK             |
| DELETE | /tasks/{task_id}   | Remove uma tarefa           | 204 No Content     |

## Estrutura do projeto

```
taskflow-api/
├── app/
│   ├── main.py          # Rotas e inicialização da aplicação
│   ├── models.py         # Modelos SQLAlchemy (tabelas)
│   ├── schemas.py         # Schemas Pydantic (validação)
│   ├── database.py        # Configuração da conexão com o banco
│   └── security.py        # Hash de senha e geração/validação de JWT
├── alembic/                # Migrações do banco de dados
├── tests/                  # Testes automatizados (pytest)
├── .github/workflows/      # Pipeline de CI (GitHub Actions)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```