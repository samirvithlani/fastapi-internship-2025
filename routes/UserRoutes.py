from fastapi import APIRouter
from controllers.UserController import addUser,getAllUsers,loginUser,forgotPassword,resetPassword
from models.UserModel import User,UserOut,UserLogin,ResetPasswordReq

router = APIRouter()

@router.post("/user/")
async def post_user(user:User):
    return await addUser(user)

@router.get("/users/")
async def get_users():
    return await getAllUsers()

@router.post("/user/login/")
async def login_user(user:UserLogin):
    return await loginUser(user)

@router.post("/forgotpassword")
async def forgot_password(email:str):
    return await forgotPassword(email)

@router.post("/resetpassword")
async def reset_password(data:ResetPasswordReq):
    return await resetPassword(data)