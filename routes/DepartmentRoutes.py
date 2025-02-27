from fastapi import APIRouter
from controllers.DepartmentController import addDepartment,getAllDepartments
from models.DepartmentModel import Department,DepartmentOut


#create an object of fastapiRouter
router = APIRouter()

@router.post("/dept/")
async def post_createDepartment(department:Department):
    return await addDepartment(department)

@router.get("/dept/")
async def get_departments():
    return await getAllDepartments()