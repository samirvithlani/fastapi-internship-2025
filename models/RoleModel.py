from pydantic import BaseModel,Field,validator
from bson import ObjectId

#_id:field pk obbjectId

class Role(BaseModel):
    name:str
    description:str


#response class
class RoleOut(Role):
    id:str =Field(alias="_id")  
    
    @validator("id", pre=True, always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)  
        
        return v