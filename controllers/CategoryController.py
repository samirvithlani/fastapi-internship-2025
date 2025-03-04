from models.CategoryModel import Category,CategoryOut
from bson import ObjectId
from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from config.database import category_collection

async def addCategory(category:Category):
    savedCategory = await category_collection.insert_one(category.dict())
    return JSONResponse(content={"message":"category saved successfully!!"},status_code=201)


async def getAllCategories():
    categories = await category_collection.find().to_list()
    return [CategoryOut(**cat) for cat in categories]
