from fastapi import FastAPI

from api.routes.analytics import router as analytics_router
from api.routes.districts import router as districts_router
from api.routes.health import router as health_router
from api.routes.predictions import router as predictions_router
from api.routes.recommendations import router as recommendations_router
from core.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


app.include_router(health_router, prefix="/api/v1")
app.include_router(districts_router, prefix="/api/v1")
app.include_router(predictions_router, prefix="/api/v1")
app.include_router(analytics_router, prefix="/api/v1")
app.include_router(recommendations_router, prefix="/api/v1")
