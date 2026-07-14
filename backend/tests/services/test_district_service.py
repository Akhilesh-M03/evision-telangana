import pytest
from fastapi import HTTPException
from sqlmodel import Session

from models.district import District
from services.district_service import district_service

def test_get_district_by_name(session: Session):
    district = District(district_name="Hyderabad")
    session.add(district)
    session.commit()
    
    result = district_service.get_district_by_name(session, "Hyderabad")
    assert result.district_name == "Hyderabad"

def test_get_district_not_found(session: Session):
    with pytest.raises(HTTPException) as excinfo:
        district_service.get_district_by_name(session, "Nonexistent")
    assert excinfo.value.status_code == 404
