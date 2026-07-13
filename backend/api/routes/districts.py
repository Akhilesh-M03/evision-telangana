from fastapi import APIRouter, Query, status

router = APIRouter(
    prefix="/districts",
    tags=["Districts"],
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_districts():
    return {
        "success": True,
        "message": "Districts retrieved successfully.",
        "data": [],
        "metadata": {"count": 0},
    }


@router.get(
    "/search",
    summary="Search districts",
    description="Search districts by name",
    status_code=status.HTTP_200_OK,
)
async def search_districts(
    q: str = Query(..., description="Search text")
):
    return {
        "success": True,
        "message": "Search completed successfully.",
        "data": [],
    }


@router.get(
    "/{district}/comparison",
    summary="Compare districts",
    description="Retrieve comparison details for a district.",
    status_code=status.HTTP_200_OK,
)
async def compare_district(
    district: str,
    compareWith: str = Query(..., description="District to compare against"),
):
    return {
        "success": True,
        "message": "District comparison generated successfully.",
        "data": {
            "districtA": {
                "name": district,
                "priorityScore": None,
                "predictedDemand": None,
                "cluster": None,
            },
            "districtB": {
                "name": compareWith,
                "priorityScore": None,
                "predictedDemand": None,
                "cluster": None,
            },
        }
    }


@router.get(
    "/{district}",
    summary="Get district by name",
    description="Retrieve information for a single district.",
    status_code=status.HTTP_200_OK,
)
async def get_district(district: str):
    return {
        "success": True,
        "message": "District information retrieved successfully.",
        "data": {
            "district": district,
            "cluster": None,
            "chargingStations": None,
            "predictedDemand": None,
            "priorityScore": None,
        },
    }
