def test_register_user(client):
    response = client.post("/register",json={
        "email": "teste@teste.com",
        "password": "senha123"
    })

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "teste@teste.com"
    assert "id" in data
    assert "password" not in data


def test_register_duplicate_email(client):
    client.post("/register", json={"email": "dup@teste.com", "password": "senha123"})
    response = client.post("/register", json={"email": "dup@teste.com", "password": "outrasenha"})

    assert response.status_code == 400


def test_login_success(client):
    client.post("/register", json={"email": "login@teste.com", "password": "senha123"})

    response = client.post("/login", data={
        "username": "login@teste.com",
        "password": "senha123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_wrong_password(client):
    client.post("/register", json={"email": "errado@teste.com", "password": "senha123"})

    response = client.post("/login", data={
        "username": "errado@teste.com",
        "password": "senhaerrada"
    })

    assert response.status_code == 401
