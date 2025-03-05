from pydantic import BaseModel, Field,validator
from typing import List, Optional,Dict,Any
from bson import ObjectId

class Product(BaseModel):
    name:Optional[str]
    price:Optional[float]
    category_id:Optional[str]
    sub_category_id:Optional[str]
    image_url:Optional[str]
    vendor_id:Optional[str]
    