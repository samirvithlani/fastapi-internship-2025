from pydantic import BaseModel,Field,validator
from bson import ObjectId

class User(BaseModel):
    firstName:str
    lastName:str
    age:int
    status:bool


class UserOut(User):
    id:str = Field(alias="_id")    
    
    @validator("id",pre=True,always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        
        return v
    