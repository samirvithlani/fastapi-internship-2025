from pydantic import BaseModel,Field,validator
from bson import ObjectId

class Department(BaseModel):
    name:str
    desc:str


class DepartmentOut(Department):
    id:str = Field(alias="_id")    
    
    @validator("id",pre=True,always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v