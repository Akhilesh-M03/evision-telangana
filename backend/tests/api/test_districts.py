from fastapi.testclient import TestClient
from sqlmodel import Session

from models.district import District

def test_get_districts_empty(client: TestClient):
    response = client.get("/api/v1/districts")
    assert response.status_code == 200
    assert response.json()["items"] == []
    assert response.json()["total"] == 0

def test_get_districts(client: TestClient, session: Session):
    session.add(District(district_name="Hyderabad"))
    session.commit()
    
    response = client.get("/api/v1/districts")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1
    assert data["items"][0]["district_name"] == "Hyderabad"
