# Unit tests for the items route of the API
from fastapi.testclient import TestClient


def test_create_item(client: TestClient):
    # First, create a user
    user_data = {"email": "test@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user_data)
    print(f"response: {response.json()}")
    user_id = response.json()["id"]

    # Then, create an item for that user
    item_data = {"title": "Test Item", "description": "This is a test item"}
    headers = {"Authorization": f"Bearer {user_id}"}
    response = client.post("/items/", json=item_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    print(f"DDD data: {data}")
    assert data["title"] == item_data["title"]
    assert data["description"] == item_data["description"]
    assert data["owner_id"] == user_id


def test_read_items(client: TestClient):
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)