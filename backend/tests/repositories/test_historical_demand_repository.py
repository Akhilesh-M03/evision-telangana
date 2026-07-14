from sqlmodel import Session
from models.district import District
from models.historical_demand import HistoricalDemand
from repositories.historical_demand_repository import historical_demand_repository

def test_get_total_demand_by_district(session: Session):
    district = District(district_name="Test District")
    session.add(district)
    session.commit()
    
    demand1 = HistoricalDemand(district_id=district.id, reporting_month="2024-01", demand_kwh=100.5)
    demand2 = HistoricalDemand(district_id=district.id, reporting_month="2024-02", demand_kwh=200.5)
    session.add(demand1)
    session.add(demand2)
    session.commit()
    
    total = historical_demand_repository.get_total_demand_by_district(session, district.id)
    assert total == 301.0

def test_get_monthly_trend(session: Session):
    district1 = District(district_name="Dist 1")
    session.add(district1)
    session.commit()
    
    demand1 = HistoricalDemand(district_id=district1.id, reporting_month="2024-01", demand_kwh=100)
    demand2 = HistoricalDemand(district_id=district1.id, reporting_month="2024-02", demand_kwh=50)
    demand3 = HistoricalDemand(district_id=district1.id, reporting_month="2024-03", demand_kwh=200)
    session.add_all([demand1, demand2, demand3])
    session.commit()
    
    trends = dict(historical_demand_repository.get_monthly_trend(session))
    assert trends["2024-01"] == 100.0
    assert trends["2024-02"] == 50.0
    assert trends["2024-03"] == 200.0
