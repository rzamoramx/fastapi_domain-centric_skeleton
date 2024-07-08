# Unit tests for the users route of the API
from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    user_data = {"email": "test@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert "id" in data


def test_read_users_me(client: TestClient):
    # First, create a user
    user_data = {"email": "test2@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user_data)
    user_id = response.json()["id"]

    # Then, simulate a request to /users/me
    headers = {"Authorization": f"Bearer {user_id}"}
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["id"] == user_id