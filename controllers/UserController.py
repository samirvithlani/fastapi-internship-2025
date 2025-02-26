from models.UserModel import User,UserOut
from bson import ObjectId
from config.database import user_collection

async def addUser(user:User):
    result = await user_collection.insert_one(user.dict())
    return {"Message":"user created successfully"}