from sqlmodel import SQLModel

# Import all models to ensure they are registered on the metadata
from models.application_metadata import ApplicationMetadata
from models.charging_stations import ChargingStation
from models.district import District
from models.district_analytics import DistrictAnalytics
from models.district_prediction import DistrictPrediction
from models.district_recommendation import DistrictRecommendation
from models.historical_demand import HistoricalDemand

__all__ = [
    "SQLModel",
    "ApplicationMetadata",
    "ChargingStation",
    "District",
    "DistrictAnalytics",
    "DistrictPrediction",
    "DistrictRecommendation",
    "HistoricalDemand",
]
