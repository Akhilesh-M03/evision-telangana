from typing import Any

from fastapi import APIRouter, Depends, Path, Query, status

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


def get_analytics_service() -> Any:
    """
    Placeholder for AnalyticsService.
    Replace with the actual service implementation later.
    """
    raise NotImplementedError("AnalyticsService is not implemented yet.")


@router.get(
    "/clusters",
    summary="Get cluster assignments",
    description="Retrieve district cluster assignments.",
    status_code=status.HTTP_200_OK,
)
async def get_cluster_assignments(
    analytics_service: Any = Depends(get_analytics_service),
):
    return await analytics_service.get_cluster_assignments()


@router.get(
    "/trends",
    summary="Get demand trends",
    description="Retrieve historical demand trends.",
    status_code=status.HTTP_200_OK,
)
async def get_demand_trends(
    district: str | None = Query(None, description="District name"),
    year: int | None = Query(None, ge=1900),
    analytics_service: Any = Depends(get_analytics_service),
):
    return await analytics_service.get_demand_trends(
        district=district,
        year=year,
    )


@router.get(
    "/profile/{district}",
    summary="Get district profile",
    description="Retrieve analytical profile of a district.",
    status_code=status.HTTP_200_OK,
)
async def get_district_profile(
    district: str = Path(..., description="District name"),
    analytics_service: Any = Depends(get_analytics_service),
):
    return await analytics_service.get_district_profile(district)


@router.get(
    "/statistics",
    summary="Get analytics statistics",
    description="Retrieve analytics summary statistics.",
    status_code=status.HTTP_200_OK,
)
async def get_analytics_statistics(
    analytics_service: Any = Depends(get_analytics_service),
):
    return await analytics_service.get_analytics_statistics()