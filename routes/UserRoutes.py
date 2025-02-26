from fastapi import APIRouter
from controllers.UserController import addUser
from models.UserModel import User,UserOut

router = APIRouter()

@router.post("/user/")
async def post_user(user:User):
    return await addUser(user)