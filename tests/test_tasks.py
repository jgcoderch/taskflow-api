def register_and_login(client, email="user@teste.com", password="senha123"):
    client.post("/register", json={"email": email, "password": password})
    response = client.post("/login", data={"username": email, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_task(client):
    headers = register_and_login(client)

    response = client.post("/tasks", json={
        "title": "Estudar pytest",
        "description": "Praticar testes automatizados"
    }, headers=headers)

    assert response.status_code == 201
    data = response.json()
    assert data ["title"] == "Estudar pytest"
    assert data ["done"] is False


def test_create_task_without_auth(client):
    response = client.post("/tasks", json={"title": "Sem login", "description": ""})

    assert response.status_code == 401


def test_list_tasks_only_shows_own(client):
    headers_a = register_and_login(client, "a@teste.com", "senha123")
    headers_b = register_and_login(client, "b@teste.com", "senha123")

    client.post("/tasks", json={"title": "Tarefa do A", "description": ""}, headers=headers_a)

    response = client.get("/tasks", headers=headers_b)

    assert response.status_code == 200
    assert response.json() == []


def test_update_task_partial_done_toggle(client):
    headers = register_and_login(client, "toggle@teste.com", "senha123")

    created = client.post("/tasks", json={
        "title": "Tarefa",
        "description": "desc"
    }, headers=headers)
    task_id = created.json()["id"]

    response = client.put(f"/tasks/{task_id}", json={"done": True}, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True
    assert data["title"] == "Tarefa"
    assert data["description"] == "desc"


def test_cannot_delete_others_task(client):
    headers_a = register_and_login(client, "dono@teste.com", "senha123")
    headers_b = register_and_login(client, "invasor@teste.com", "senha123")

    created = client.post("/tasks", json={"title": "Protegida", "description": ""}, headers=headers_a)
    task_id = created.json()["id"]

    response = client.delete(f"/tasks/{task_id}", headers=headers_b)

    assert response.status_code == 404

    