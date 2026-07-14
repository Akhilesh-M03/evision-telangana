from fastapi import APIRouter

from api.routes.analytics import router as analytics_router
from api.routes.districts import router as districts_router
from api.routes.health import router as health_router
from api.routes.predictions import router as predictions_router
# from api.routes.recommendations import router as recommendations_router
from api.routes.charging_stations import router as charging_stations_router
from api.routes.dashboard import router as dashboard_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(districts_router)
api_router.include_router(charging_stations_router)
api_router.include_router(dashboard_router)
api_router.include_router(analytics_router)
api_router.include_router(predictions_router)
# api_router.include_router(recommendations_router) # commented out since we are not implementing it yet
