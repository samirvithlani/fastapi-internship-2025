from models.UserModel import User,UserOut
from bson import ObjectId
from config.database import user_collection,role_collection

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
    #print(users)
    for user in users:
        #print(user)#single user object..
        role = await role_collection.find_one({"_id":user["role_id"]}) #rolid
        #print("role...",role)
        user["role"] = role
        #print("user.....",user)
    #return {"ok":"ok"}
    return [UserOut(**user) for user in users]