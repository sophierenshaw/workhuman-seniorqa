from fastapi.testclient import TestClient

from .api import app

client = TestClient(app)

def test_query_with_valid_input():
    response = client.get("/query?query=Hello")
    assert response.status_code == 200
    assert response.json() == {"message": f"Query received: Hello"}

def test_query_with_empty_input():
    response = client.get("/query?query=")
    assert response.status_code == 400
    assert response.json() == {"detail": "Query parameter is required"}

def test_query_without_input():
    response = client.get("/query")
    assert response.status_code == 422