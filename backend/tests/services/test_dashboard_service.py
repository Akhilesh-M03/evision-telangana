from sqlmodel import Session

from services.dashboard_service import dashboard_service

def test_get_overview(session: Session):
    overview = dashboard_service.get_overview(session)
    assert overview.statistics is not None
    assert overview.recent_activity is None

def test_get_stations_summary(session: Session):
    summary = dashboard_service.get_stations_summary(session)
    assert summary.total >= 0

def test_get_trends_summary(session: Session):
    trends = dashboard_service.get_trends_summary(session)
    assert isinstance(trends.monthly_demand, list)
