from pydantic import BaseModel, Field,validator
from typing import List, Optional,Dict,Any,Annotated
from bson import ObjectId
from fastapi import File, UploadFile,Form

class Product(BaseModel):
    name:Optional[str]
    price:Optional[float]
    category_id:Optional[str]
    sub_category_id:Optional[str]
    image_url:Optional[str]=None
    vendor_id:Optional[str]
    #accept file
    image:UploadFile = File(...)
    

class ProductOut(BaseModel):
    id: str = Field(alias="_id")
    name: Optional[str]
    price: Optional[float]
    category_id: Optional[str]
    sub_category_id: Optional[str]
    image_url: Optional[str] = None
    vendor_id: Optional[str]
    category: Optional[Dict[str, Any]] = None
    sub_category: Optional[Dict[str, Any]] = None
    vendor: Optional[Dict[str, Any]] = None

    @validator("id", "category_id", "sub_category_id", "vendor_id", pre=True, always=True)
    def convert_objectid_to_str(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v
    
    @validator("category", "sub_category", "vendor", pre=True, always=True)
    def convert_nested_objectid(cls, v):
        if isinstance(v, dict) and "_id" in v:
            v["_id"] = str(v["_id"])  
        return v        
    
    