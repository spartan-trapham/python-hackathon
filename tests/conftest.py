import pytest
from fastapi.testclient import TestClient

from src.fast_api_app import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c