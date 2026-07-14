from typing import Any

from pydantic import BaseModel


class TrendDataPoint(BaseModel):
    month: str
    value: float


class DistrictProfile(BaseModel):
    district_name: str
    total_stations: int
    total_historical_demand_kwh: float
    avg_monthly_demand_kwh: float


class OverallStatistics(BaseModel):
    total_districts: int
    total_charging_stations: int
    total_energy_demand_kwh: float


class DashboardOverviewResponse(BaseModel):
    statistics: OverallStatistics
    recent_activity: list[Any] | None = None  # Placeholder for future


class DashboardStationsResponse(BaseModel):
    total: int
    by_organization: dict[str, int]


class DashboardTrendsResponse(BaseModel):
    monthly_demand: list[TrendDataPoint]
