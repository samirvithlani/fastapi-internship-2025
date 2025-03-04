from pydantic import BaseModel,Field,validator
from typing import List, Optional,Dict,Any
from bson import ObjectId

class Category(BaseModel):
    name: str
    description: str


class CategoryOut(Category):
    id:str = Field(alias='_id')
    
    @validator('id', pre=True, always=True)
    def convert_obectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v
        