from fastapi.testclient import TestClient

def test_health(client: TestClient) -> None :
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_users(client: TestClient) -> None:
    response = client.get('/api/users/c2667213-c3b2-4a8a-b47a-ea8bd3173e49')
    assert response.status_code == 404
    assert response.json() == {'error': {'code': 'APP-0201', 'message': 'User not found.'}}
