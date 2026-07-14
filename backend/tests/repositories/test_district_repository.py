from sqlmodel import Session
from models.district import District
from repositories.district_repository import district_repository

def test_create_and_get_district(session: Session):
    district = District(district_name="Hyderabad")
    session.add(district)
    session.commit()
    
    db_district = district_repository.get_by_name(session, "Hyderabad")
    assert db_district is not None
    assert db_district.district_name == "Hyderabad"

def test_search_districts(session: Session):
    districts = [
        District(district_name="Hyderabad"),
        District(district_name="Ranga Reddy"),
        District(district_name="Medchal-Malkajgiri")
    ]
    for d in districts:
        session.add(d)
    session.commit()
    
    results = district_repository.search(session, "Reddy")
    assert len(results) == 1
    assert results[0].district_name == "Ranga Reddy"
