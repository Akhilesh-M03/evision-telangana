from fastapi.testclient import TestClient
from sqlmodel import Session

from models.district import District
from models.charging_stations import ChargingStation

def test_get_charging_stations_empty(client: TestClient):
    response = client.get("/api/v1/charging-stations")
    assert response.status_code == 200
    assert response.json()["items"] == []

def test_get_charging_station_by_id(client: TestClient, session: Session):
    district = District(district_name="Test District")
    session.add(district)
    session.commit()
    
    station = ChargingStation(district_id=district.id, station_name="Test Station")
    session.add(station)
    session.commit()
    
    response = client.get(f"/api/v1/charging-stations/{station.id}")
    assert response.status_code == 200
    assert response.json()["station_name"] == "Test Station"
