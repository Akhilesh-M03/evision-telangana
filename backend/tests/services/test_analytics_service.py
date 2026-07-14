import pytest
from fastapi import HTTPException
from sqlmodel import Session

from models.district import District
from models.historical_demand import HistoricalDemand
from services.analytics_service import analytics_service

def test_get_overall_statistics(session: Session):
    district = District(district_name="Dist 1")
    session.add(district)
    session.commit()
    
    demand = HistoricalDemand(district_id=district.id, reporting_month="2024-01", demand_kwh=150)
    session.add(demand)
    session.commit()
    
    stats = analytics_service.get_overall_statistics(session)
    assert stats["total_districts"] == 1
    assert stats["total_energy_demand_kwh"] == 150.0

def test_get_district_profile_not_found(session: Session):
    with pytest.raises(HTTPException) as excinfo:
        analytics_service.get_district_profile(session, "Nonexistent")
    assert excinfo.value.status_code == 404
