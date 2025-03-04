from fastapi import APIRouter
from controllers.StateController import addState,getStates
from models.StateModel import State,StateOut

router = APIRouter()

@router.post("/addState/")
async def post_state(state:State):
    return await addState(state)

@router.get("/getStates/")
async def get_states():
    return await getStates()

