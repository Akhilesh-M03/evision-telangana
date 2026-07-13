from typing import Any

from fastapi import APIRouter, Depends, Path, Query, status

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


def get_recommendation_service() -> Any:
    """
    Placeholder for RecommendationService.
    Replace with the actual service once implemented.
    """
    raise NotImplementedError("RecommendationService is not implemented yet.")


@router.get(
    "/",
    summary="Get all recommendations",
    description="Retrieve recommendations for all districts.",
    status_code=status.HTTP_200_OK,
)
async def get_all_recommendations(
    priority: str | None = Query(None, description="Filter by priority"),
    limit: int | None = Query(None, ge=1, description="Maximum records"),
    recommendation_service: Any = Depends(get_recommendation_service),
):
    return await recommendation_service.get_all_recommendations(
        priority=priority,
        limit=limit,
    )


@router.get(
    "/high-priority",
    summary="Get high priority recommendations",
    description="Retrieve high priority districts.",
    status_code=status.HTTP_200_OK,
)
async def get_high_priority_recommendations(
    limit: int | None = Query(None, ge=1),
    recommendation_service: Any = Depends(get_recommendation_service),
):
    return await recommendation_service.get_high_priority_recommendations(limit=limit)


@router.get(
    "/summary",
    summary="Recommendation summary",
    description="Retrieve recommendation summary.",
    status_code=status.HTTP_200_OK,
)
async def get_recommendation_summary(
    recommendation_service: Any = Depends(get_recommendation_service),
):
    return await recommendation_service.get_summary()


@router.get(
    "/download",
    summary="Download recommendations",
    description="Download recommendation report.",
    status_code=status.HTTP_200_OK,
)
async def download_recommendations(
    recommendation_service: Any = Depends(get_recommendation_service),
):
    return await recommendation_service.download_recommendations()


@router.get(
    "/{district_id}",
    summary="Get recommendation by district",
    description="Retrieve recommendation for a specific district.",
    status_code=status.HTTP_200_OK,
)
async def get_recommendation_by_district(
    district_id: int = Path(..., ge=1, description="District ID"),
    recommendation_service: Any = Depends(get_recommendation_service),
):
    return await recommendation_service.get_recommendation_by_district(district_id)