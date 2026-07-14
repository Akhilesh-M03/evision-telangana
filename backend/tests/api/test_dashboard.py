from fastapi.testclient import TestClient

def test_get_dashboard_overview(client: TestClient):
    response = client.get("/api/v1/dashboard/overview")
    assert response.status_code == 200
    data = response.json()
    assert "statistics" in data
    assert data["recent_activity"] is None

def test_get_dashboard_stations(client: TestClient):
    response = client.get("/api/v1/dashboard/stations")
    assert response.status_code == 200
    assert "total" in response.json()

def test_get_dashboard_trends(client: TestClient):
    response = client.get("/api/v1/dashboard/trends")
    assert response.status_code == 200
    assert "monthly_demand" in response.json()
