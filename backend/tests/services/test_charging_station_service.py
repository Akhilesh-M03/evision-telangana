import pytest
from fastapi import HTTPException
from sqlmodel import Session

from models.district import District
from models.charging_stations import ChargingStation
from services.charging_station_service import charging_station_service

def test_get_station_by_id(session: Session):
    district = District(district_name="Dist 1")
    session.add(district)
    session.commit()
    
    station = ChargingStation(district_id=district.id, station_name="Station X")
    session.add(station)
    session.commit()
    
    result = charging_station_service.get_station_by_id(session, station.id)
    assert result.station_name == "Station X"

def test_get_station_not_found(session: Session):
    with pytest.raises(HTTPException) as excinfo:
        charging_station_service.get_station_by_id(session, 999)
    assert excinfo.value.status_code == 404

def test_get_all_stations_with_invalid_district(session: Session):
    with pytest.raises(HTTPException) as excinfo:
        charging_station_service.get_all_stations(session, district_id=999)
    assert excinfo.value.status_code == 404
