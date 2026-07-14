from fastapi.testclient import TestClient

def test_get_overall_statistics(client: TestClient):
    response = client.get("/api/v1/analytics/statistics")
    assert response.status_code == 200
    data = response.json()
    assert "total_districts" in data
    assert "total_charging_stations" in data

def test_get_trends(client: TestClient):
    response = client.get("/api/v1/analytics/trends")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_profile_not_found(client: TestClient):
    response = client.get("/api/v1/analytics/profile/Nonexistent")
    assert response.status_code == 404
