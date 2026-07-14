from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from sqlalchemy import text

from database.session import get_session
from schemas.health import HealthResponse, HealthLiveResponse, HealthReadyResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    response_model=HealthResponse,
    summary="Health Check",
    description="Check if the backend service is running.",
    status_code=status.HTTP_200_OK,
)
async def health_check():
    return HealthResponse(status="Healthy", apiVersion="v1")


@router.get(
    "/live",
    response_model=HealthLiveResponse,
    summary="Liveness Probe",
    description="Check if the application is alive.",
    status_code=status.HTTP_200_OK,
)
async def health_live():
    return HealthLiveResponse(status="Alive")


@router.get(
    "/ready",
    response_model=HealthReadyResponse,
    summary="Readiness Probe",
    description="Check if the application is ready to serve traffic (checks DB connection).",
    status_code=status.HTTP_200_OK,
)
async def health_ready(session: Session = Depends(get_session)):
    try:
        session.exec(text("SELECT 1")).one()
        return HealthReadyResponse(status="Ready", database="Connected")
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=503, detail=f"Database unavailable: {str(e)}")
