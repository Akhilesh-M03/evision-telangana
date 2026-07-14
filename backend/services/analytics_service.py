from fastapi import HTTPException
from sqlmodel import Session

from repositories.district_repository import district_repository
from repositories.charging_station_repository import charging_station_repository
from repositories.historical_demand_repository import historical_demand_repository
from schemas.analytics import DistrictProfile, TrendDataPoint


class AnalyticsService:
    def get_overall_statistics(self, session: Session) -> dict:
        total_districts = district_repository.count(session)
        total_stations = charging_station_repository.count(session)
        total_demand = historical_demand_repository.get_total_demand(session)
        
        return {
            "total_districts": total_districts,
            "total_charging_stations": total_stations,
            "total_energy_demand_kwh": total_demand
        }

    def get_district_profile(self, session: Session, district_name: str) -> DistrictProfile:
        district = district_repository.get_by_name(session, district_name)
        if not district:
            raise HTTPException(status_code=404, detail=f"District {district_name} not found")
            
        stations = charging_station_repository.get_by_district(session, district.id) # type: ignore
        total_stations = len(stations)
        
        demand = historical_demand_repository.get_total_demand_by_district(session, district.id) # type: ignore
        
        # Calculate average monthly demand (simplified to demand / months of data)
        history = historical_demand_repository.get_by_district(session, district.id, limit=1000) # type: ignore
        avg_demand = demand / len(history) if history else 0.0
        
        return DistrictProfile(
            district_name=district_name,
            total_stations=total_stations,
            total_historical_demand_kwh=demand,
            avg_monthly_demand_kwh=avg_demand
        )

    def get_demand_trends(self, session: Session) -> list[TrendDataPoint]:
        trends = historical_demand_repository.get_monthly_trend(session)
        return [TrendDataPoint(month=month, value=value) for month, value in trends]

analytics_service = AnalyticsService()
