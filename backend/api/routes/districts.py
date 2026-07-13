from fastapi import APIRouter,Query

router=APIRouter(
    prefix="/districts",
    tags=["Districts"],
)

@router.get("/")
async def get_all_districts():
    return{
        "success":True,
        "message": "district retrieved  succesfully ",
        "data":[]
    }

@router.get("/{district_id}")
async def get_all_district_id(district_id:int):
    return{
        "success":True,
        "message":"District fecthed succesfully",
        "data":[]
    }
@router.get("/search",
            summary="search_districts",
            description="search districts by name"
            )
async def search_districts(
    name : str=Query(description="district name")
):
    return{
        "sucess":True,
        "message":"distict name found sucesfully",
        "data":{
            "search":name
        }
    }

@router.get(
    "/{district_id}/comparison",
    summary="Compare district",
    description="Retrieve comparison details for a district."
)
async def compare_district(district_id: int):
    return {
        "success": True,
        "message": "Comparison retrieved successfully.",
        "data": {
            "district_id": district_id
        }
    }
