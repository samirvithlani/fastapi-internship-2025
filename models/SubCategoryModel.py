from pydantic import BaseModel,Field,validator
from typing import List, Optional,Dict,Any
from bson import ObjectId

class SubCategory(BaseModel):
    name: str
    description: str
    category_id:str
    

class SubCategoryOut(SubCategory):
    id:str = Field(alias='_id') 
    category_id: Optional[Dict[str,Any]] = None #{_id:"",name,desc,cate_id:{_id:"",name,desc}}
    
    @validator('id', pre=True, always=True)
    def convert_obectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v
    
    @validator('category_id', pre=True, always=True)
    def convert_categoryId(cls,v):
        if isinstance(v,Dict) and "_id" in v:
            v["_id"] = str(v["_id"])
        return v
    