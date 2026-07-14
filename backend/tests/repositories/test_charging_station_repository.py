from sqlmodel import Session
from models.district import District
from models.charging_stations import ChargingStation
from repositories.charging_station_repository import charging_station_repository

def test_get_by_district(session: Session):
    district = District(district_name="Test District")
    session.add(district)
    session.commit()
    
    station = ChargingStation(district_id=district.id, station_name="Station A", organization="Org1")
    session.add(station)
    session.commit()
    
    results = charging_station_repository.get_by_district(session, district.id)
    assert len(results) == 1
    assert results[0].station_name == "Station A"

def test_count_by_organization(session: Session):
    district = District(district_name="Test District")
    session.add(district)
    session.commit()
    
    station1 = ChargingStation(district_id=district.id, station_name="Station A", organization="Org1")
    station2 = ChargingStation(district_id=district.id, station_name="Station B", organization="Org1")
    station3 = ChargingStation(district_id=district.id, station_name="Station C", organization="Org2")
    for s in [station1, station2, station3]:
        session.add(s)
    session.commit()
    
    counts = dict(charging_station_repository.count_by_organization(session))
    assert counts.get("Org1") == 2
    assert counts.get("Org2") == 1
