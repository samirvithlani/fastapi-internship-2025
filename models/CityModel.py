from pydantic import BaseModel,Field,validator
from typing import List, Optional,Dict,Any
from bson import ObjectId

class City(BaseModel):
    name: str
    state_id:str
    


class CityOut(City):
    id:str = Field(alias="_id")
    state:Optional[Dict[str,Any]] = None    
    
    @validator("id",pre=True,always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v
    
    @validator("state", pre=True, always=True)
    def convert_state(cls, v):
        if isinstance(v, dict) and "_id" in v:
            v["_id"] = str(v["_id"])  # Convert role _id to string
        return v