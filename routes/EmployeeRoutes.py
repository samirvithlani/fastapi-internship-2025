from fastapi import APIRouter
from controllers.EmployeeController import createEmployee,getAllEmployee
from models.EmployeeModel import Employee,EmployeeOut

router = APIRouter()

@router.post("/emp/")
async def post_employee(employee:Employee):
    return await createEmployee(employee)

@router.get('/emp/')
async def get_employee():
    return await getAllEmployee()