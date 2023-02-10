import pytest
from fastapi.testclient import TestClient
from app.main import new_app


settings = {
    "app": {
        "name": "Test App",
        "version": "0.0.1",
    }
}


@pytest.fixture
def app():
    app = new_app(settings)
    yield app


@pytest.fixture
def client(app):
    return TestClient(app)
