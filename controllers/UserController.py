from models.UserModel import User,UserOut
from bson import ObjectId
from config.database import user_collection,role_collection
from fastapi import HTTPException
import bcrypt

async def addUser(user:User):
    #typeCast
    #print("user....",user.role_id)
    #convert string id to object it comp.,, to mongo db
    user.role_id = ObjectId(user.role_id)
    print("after type cast",user.role_id)
    result = await user_collection.insert_one(user.dict())
    return {"Message":"user created successfully"}

# async def getAllUsers():
#     users = await user_collection.find().to_list()
#     print("users",users)
#     return [UserOut(**user) for user in users]

async def getAllUsers():
    users = await user_collection.find().to_list(length=None)

    for user in users:
        # Convert role_id from ObjectId to str before validation
        if "role_id" in user and isinstance(user["role_id"], ObjectId):
            user["role_id"] = str(user["role_id"])
        
        # Fetch role details
        role = await role_collection.find_one({"_id": ObjectId(user["role_id"])})  
        
        if role:
            role["_id"] = str(role["_id"])  # Convert role _id to string
            user["role"] = role

    return [UserOut(**user) for user in users]

async def loginUser(email:str,password:str):
    #norma; password : plain text --> encr
    foundUser = await user_collection.find_one({"email":email})
    if foundUser is None:
        raise HTTPException(status_code=404,detail="User not found")
    
    #compare password
    if "password" in foundUser and bcrypt.checkpw(password.encode(),foundUser["password"].encode()):
        return {"message":"user login success"}
        
    else:
        raise HTTPException(status_code=404,detail="Invalid password")
    
