from sqlmodel import Session

from schemas.analytics import (
    DashboardOverviewResponse,
    DashboardStationsResponse,
    DashboardTrendsResponse,
    OverallStatistics
)
from services.analytics_service import analytics_service
from repositories.charging_station_repository import charging_station_repository


class DashboardService:
    def get_overview(self, session: Session) -> DashboardOverviewResponse:
        stats_dict = analytics_service.get_overall_statistics(session)
        stats = OverallStatistics(**stats_dict)
        return DashboardOverviewResponse(statistics=stats, recent_activity=None)

    def get_stations_summary(self, session: Session) -> DashboardStationsResponse:
        total = charging_station_repository.count(session)
        org_counts = charging_station_repository.count_by_organization(session)
        
        by_org = {org: count for org, count in org_counts if org}
        return DashboardStationsResponse(total=total, by_organization=by_org)

    def get_trends_summary(self, session: Session) -> DashboardTrendsResponse:
        trends = analytics_service.get_demand_trends(session)
        return DashboardTrendsResponse(monthly_demand=trends)

dashboard_service = DashboardService()
