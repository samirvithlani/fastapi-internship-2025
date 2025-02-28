from fastapi import APIRouter
from controllers.UserController import addUser,getAllUsers,loginUser
from models.UserModel import User,UserOut

router = APIRouter()

@router.post("/user/")
async def post_user(user:User):
    return await addUser(user)

@router.get("/users/")
async def get_users():
    return await getAllUsers()

@router.get("/user/login/")
async def login_user(email:str,password:str):
    return await loginUser(email,password)