from models.DepartmentModel import Department,DepartmentOut
from bson import ObjectId
from config.database import department_collection

#department add function

async def addDepartment(department:Department):
    result = await department_collection.insert_one(department.dict())
    return {"message":"Department created.."}

async def getAllDepartments():
    departments = await department_collection.find().to_list()
    return [DepartmentOut(**dept) for dept in departments]