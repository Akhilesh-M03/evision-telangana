from fastapi import APIRouter, Query, status

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)


@router.get(
    "/",
    summary="Get all predictions",
    description="Retrieve predicted EV charging demand for all districts.",
    status_code=status.HTTP_200_OK,
)
async def get_all_predictions(year: int | None = Query(None, description="Forecast year")):
    response = {
        "success": True,
        "message": "Predictions retrieved successfully.",
        "data": [],
    }
    if year is not None:
        response["metadata"] = {"year": year}
    return response


@router.get(
    "/{district}",
    summary="Get prediction by district",
    description="Retrieve prediction for a specific district.",
    status_code=status.HTTP_200_OK,
)
async def get_prediction_by_district(district: str):
    return {
        "success": True,
        "message": "Prediction retrieved successfully.",
        "data": {
            "district": district,
            "predictedDemand": None,
        }
    }


@router.get(
    "/top",
    summary="Top priority districts",
    description="Retrieve top districts based on predicted demand.",
    status_code=status.HTTP_200_OK,
)
async def get_top_predictions(
    limit: int = Query(10, ge=1, le=50)
):
    return {
        "success": True,
        "message": "Top predictions retrieved successfully.",
        "data": [],
    }


@router.get(
    "/summary",
    summary="Prediction summary",
    description="Retrieve prediction summary statistics.",
    status_code=status.HTTP_200_OK,
)
async def get_prediction_summary():
    return {
        "success": True,
        "message": "Prediction summary retrieved successfully.",
        "data": {
            "highestPrediction": None,
            "lowestPrediction": None,
            "averagePrediction": None,
            "districtCount": 0,
        }
    }