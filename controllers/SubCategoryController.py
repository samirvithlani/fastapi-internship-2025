from models.SubCategoryModel import SubCategory,SubCategoryOut
from bson import ObjectId
from config.database import sub_category_collection,category_collection
from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse

async def addSubCategory(sub_category:SubCategory):
    savedCategory = await sub_category_collection.insert_one(sub_category.dict())
    return JSONResponse(content={"message":"SubCategory saved successfully!!"},status_code=201)

async def getAllSubCategories():
    subCategories = await sub_category_collection.find().to_list()
    
    for subCat in subCategories:
        if "category_id" in subCat and isinstance(subCat["category_id"],ObjectId):
            subCat["category_id"] = str(subCat["category_id"])
        
        category = await category_collection.find_one({"_id":ObjectId(subCat["category_id"])})
        if category:
            category["_id"] = str(category["_id"])
            subCat["category_id"] = category    
        
    
    return [SubCategoryOut(**subCat) for subCat in subCategories]        
            