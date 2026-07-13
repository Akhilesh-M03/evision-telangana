from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)


@router.get(
    "/",
    summary="Get all predictions",
    description="Retrieve predicted EV charging demand for all districts."
)
async def get_all_predictions():
    return {
        "success": True,
        "message": "Predictions retrieved successfully.",
        "data": []
    }


@router.get(
    "/{district_id}",
    summary="Get prediction by district",
    description="Retrieve prediction for a specific district."
)
async def get_prediction_by_district(district_id: int):
    return {
        "success": True,
        "message": "Prediction retrieved successfully.",
        "data": {
            "district_id": district_id
        }
    }


@router.get(
    "/top",
    summary="Top priority districts",
    description="Retrieve top districts based on predicted demand."
)
async def get_top_predictions(
    limit: int = Query(10, ge=1, le=50)
):
    return {
        "success": True,
        "message": "Top predictions retrieved successfully.",
        "data": [],
        "limit": limit
    }


@router.get(
    "/summary",
    summary="Prediction summary",
    description="Retrieve prediction summary statistics."
)
async def get_prediction_summary():
    return {
        "success": True,
        "message": "Prediction summary retrieved successfully.",
        "data": {}
    }