from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)

@router.get(
    "/",
    summary="Get all predictions",
    description="Retrieve predicted EV charging demand for all districts. TODO: Implement prediction endpoints according to the API Alignment Report.",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
async def get_all_predictions():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Prediction endpoints not implemented. See API Alignment Report."
    )

@router.get(
    "/{district}",
    summary="Get prediction by district",
    description="Retrieve prediction for a specific district. TODO: Implement prediction endpoints according to the API Alignment Report.",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
async def get_prediction_by_district(district: str):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Prediction endpoints not implemented. See API Alignment Report."
    )

@router.get(
    "/top",
    summary="Top priority districts",
    description="Retrieve top districts based on predicted demand. TODO: Implement prediction endpoints according to the API Alignment Report.",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
async def get_top_predictions():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Prediction endpoints not implemented. See API Alignment Report."
    )

@router.get(
    "/summary",
    summary="Prediction summary",
    description="Retrieve prediction summary statistics. TODO: Implement prediction endpoints according to the API Alignment Report.",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
async def get_prediction_summary():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Prediction endpoints not implemented. See API Alignment Report."
    )