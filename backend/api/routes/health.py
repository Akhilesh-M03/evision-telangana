from fastapi import APIRouter, status

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "/",
    summary="Health Check",
    description="Check if the backend service is running.",
    status_code=status.HTTP_200_OK,
)
async def health_check():
    return {
        "status": "healthy",
        "service": "EVision Telangana API",
    }


@router.get(
    "/live",
    summary="Liveness Check",
    description="Check if the application is alive.",
    status_code=status.HTTP_200_OK,
)
async def health_live():
    return {
        "status": "alive",
        "service": "EVision Telangana API",
    }


@router.get(
    "/ready",
    summary="Readiness Check",
    description="Check if the application is ready to serve requests.",
    status_code=status.HTTP_200_OK,
)
async def health_ready():
    return {
        "status": "ready",
        "service": "EVision Telangana API",
    }


@router.get(
    "/version",
    summary="API Version",
    description="Retrieve backend version information.",
    status_code=status.HTTP_200_OK,
)
async def get_version():
    return {
        "project": "EVision Telangana",
        "api_version": "v1",
        "status": "stable",
    }
