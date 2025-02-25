from fastapi import APIRouter
from models.RoleModel import Role,RoleOut
from controllers.RoleController import getAllRoles

router = APIRouter()

@router.get("/roles/")
async def get_roles():
    return await getAllRoles() #promise