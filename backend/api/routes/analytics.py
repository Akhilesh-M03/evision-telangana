from fastapi import APIRouter, Depends, Path, status
from sqlmodel import Session

from database.session import get_session
from schemas.analytics import DistrictProfile, OverallStatistics, TrendDataPoint
from services.analytics_service import analytics_service

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

@router.get(
    "/statistics",
    response_model=OverallStatistics,
    summary="Get analytics statistics",
    description="Retrieve analytics summary statistics.",
    status_code=status.HTTP_200_OK,
)
async def get_analytics_statistics(session: Session = Depends(get_session)):
    stats_dict = analytics_service.get_overall_statistics(session)
    return OverallStatistics(**stats_dict)


@router.get(
    "/profile/{district}",
    response_model=DistrictProfile,
    summary="Get district profile",
    description="Retrieve analytical profile of a district.",
    status_code=status.HTTP_200_OK,
)
async def get_district_profile(
    district: str = Path(..., description="District name"),
    session: Session = Depends(get_session)
):
    return analytics_service.get_district_profile(session, district_name=district)


@router.get(
    "/trends",
    response_model=list[TrendDataPoint],
    summary="Get demand trends",
    description="Retrieve historical demand trends.",
    status_code=status.HTTP_200_OK,
)
async def get_demand_trends(session: Session = Depends(get_session)):
    return analytics_service.get_demand_trends(session)