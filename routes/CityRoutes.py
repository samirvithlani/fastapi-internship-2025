from fastapi import APIRouter,HTTPException
from controllers import CityController #.....
from models.CityModel import City,CityOut
from bson import ObjectId

router = APIRouter()
@router.post("/city")
async def post_city(city:City):
    return await CityController.addCity(city)

@router.get("/city")
async def get_city():
    return await CityController.getCity()