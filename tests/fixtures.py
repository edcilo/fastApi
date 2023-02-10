import pytest
from fastapi.testclient import TestClient
from app.main import new_app


settings = {
    "app": {
        "app": {
            "name": "Test App",
            "version": "1.0.0",
        }
    }
}


@pytest.fixture
def app():
    app = new_app(settings)
    yield app


@pytest.fixture
def client(app):
    return TestClient(app)
