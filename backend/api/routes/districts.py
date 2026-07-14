from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session

from database.session import get_session
from schemas.district import DistrictResponse
from schemas.pagination import PaginatedResponse
from services.district_service import district_service

router = APIRouter(
    prefix="/districts",
    tags=["Districts"],
)

@router.get(
    "",
    response_model=PaginatedResponse[DistrictResponse],
    summary="Get all districts",
    status_code=status.HTTP_200_OK
)
async def get_all_districts(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    session: Session = Depends(get_session)
):
    return district_service.get_all_districts(session, skip=skip, limit=limit)


@router.get(
    "/search",
    response_model=PaginatedResponse[DistrictResponse],
    summary="Search districts",
    status_code=status.HTTP_200_OK,
)
async def search_districts(
    q: str = Query(..., description="Search text"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    session: Session = Depends(get_session)
):
    return district_service.search_districts(session, query=q, skip=skip, limit=limit)


@router.get(
    "/{district}",
    response_model=DistrictResponse,
    summary="Get district by name",
    status_code=status.HTTP_200_OK,
)
async def get_district(
    district: str,
    session: Session = Depends(get_session)
):
    return district_service.get_district_by_name(session, district_name=district)
