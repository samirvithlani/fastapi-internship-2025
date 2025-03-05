from models.CityModel import City,CityOut
from bson import ObjectId
from config.database import city_collection,state_collection
from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse


async def addCity(city:City):
    savedCity = await city_collection.insert_one(city.dict())
    return JSONResponse(content={"message":"city added"},status_code=201)


async def getCity():
    cities = await city_collection.find().to_list()
    
    for city in cities:
        if "state_id" in city and isinstance(city["state_id"], ObjectId):
            city["state_id"] = str(city["state_id"])
        
        state  = await state_collection.find_one({"_id":ObjectId(city["state_id"])})    
        if state:
            state["_id"] = str(state["_id"])
            city["state"] = state
    
    return [CityOut(**city) for city in cities]


async def getCityByStateId(state_id:str):
    print("state id",state_id)
    cities = await city_collection.find({"state_id":state_id}).to_list()
    for city in cities:
        if "state_id" in city and isinstance(city["state_id"], ObjectId):
            city["state_id"] = str(city["state_id"])
        
        state  = await state_collection.find_one({"_id":ObjectId(city["state_id"])})    
        if state:
            state["_id"] = str(state["_id"])
            city["state"] = state
    
    return [CityOut(**city) for city in cities]
    
    


