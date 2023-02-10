from fastapi.testclient import TestClient
from .fixtures import app, client, settings


def test_about_route(client):
    response = client.get("/api/v1/about")
    assert response.status_code == 200
    assert response.json() == settings["app"]["app"]
