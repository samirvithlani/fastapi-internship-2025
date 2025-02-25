from config.database import role_collection # roles
from models.RoleModel import Role,RoleOut
from bson import ObjectId

#business logic function

async def getAllRoles():
    #find --> select * from roles
    roles = await role_collection.find().to_list()
    print("roles...................",roles)
    return [RoleOut(**role) for role in roles]