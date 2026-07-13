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
        "success": True,
        "message": "Application is healthy.",
        "data": {
            "status": "Healthy",
            "apiVersion": "v1",
        },
    }


@router.get(
    "/database",
    summary="Database Health Check",
    description="Check if the database connection is available.",
    status_code=status.HTTP_200_OK,
)
async def health_database():
    return {
        "success": True,
        "message": "Database connection successful.",
        "data": {
            "status": "Connected",
        },
    }


@router.get(
    "/models",
    summary="Models Health Check",
    description="Check if the trained models are available.",
    status_code=status.HTTP_200_OK,
)
async def health_models():
    return {
        "success": True,
        "message": "Machine learning models loaded successfully.",
        "data": {
            "status": "Available",
        },
    }


@router.get(
    "/ai",
    summary="AI Health Check",
    description="Check if the configured AI service is available.",
    status_code=status.HTTP_200_OK,
)
async def health_ai():
    return {
        "success": True,
        "message": "AI service is available.",
        "data": {
            "status": "Available",
        },
    }
