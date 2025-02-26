from fastapi import APIRouter
from models.RoleModel import Role,RoleOut
from controllers.RoleController import getAllRoles,addRole,deleteRole,getRoleById

router = APIRouter()

@router.get("/roles/")
async def get_roles():
    return await getAllRoles() #promise
#{name:"",descr:""}

@router.post("/role/")
async def post_role(role:Role):
    return await addRole(role)


@router.delete("/role/{roleId}")
async def delete_role(roleId:str):
    return await deleteRole(roleId)

@router.get("/role/{roleId}")
async def get_role_byId(roleId:str):
    return await getRoleById(roleId)