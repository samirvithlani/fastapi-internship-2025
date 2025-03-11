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
    
    