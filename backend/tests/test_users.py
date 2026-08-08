from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_existing_user():
    response = client.get("/api/v1/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "email" in data
    assert "username" in data


def test_get_non_existing_user():
    response = client.get("/api/v1/users/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"