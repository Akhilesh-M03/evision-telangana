from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from database.session import get_session
from schemas.analytics import (
    DashboardOverviewResponse,
    DashboardStationsResponse,
    DashboardTrendsResponse
)
from services.dashboard_service import dashboard_service

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)

@router.get(
    "/overview",
    response_model=DashboardOverviewResponse,
    summary="Dashboard Overview",
    status_code=status.HTTP_200_OK
)
async def get_dashboard_overview(session: Session = Depends(get_session)):
    return dashboard_service.get_overview(session)

@router.get(
    "/stations",
    response_model=DashboardStationsResponse,
    summary="Dashboard Stations Summary",
    status_code=status.HTTP_200_OK
)
async def get_dashboard_stations(session: Session = Depends(get_session)):
    return dashboard_service.get_stations_summary(session)

@router.get(
    "/trends",
    response_model=DashboardTrendsResponse,
    summary="Dashboard Trends Summary",
    status_code=status.HTTP_200_OK
)
async def get_dashboard_trends(session: Session = Depends(get_session)):
    return dashboard_service.get_trends_summary(session)
