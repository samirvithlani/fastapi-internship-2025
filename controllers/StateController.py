from models.StateModel import State,StateOut
from bson import ObjectId
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from config.database import state_collection

async def addState(state:State):
    savedState = await state_collection.insert_one(state.dict())
    if savedState:
        return JSONResponse(status_code=201,content={"message:":"State Added Successfully"})
    raise HTTPException(status_code=500,detail="Internal Server Error")

async def getStates():
    states = await state_collection.find().to_list()
    #check lennght of states
    if len(states)==0:
        return JSONResponse(status_code=404,content={"message":"No State Found"})
    return [StateOut(**state) for state in states]
    
    