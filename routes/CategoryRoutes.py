from fastapi import APIRouter
from models.CategoryModel import Category,CategoryOut
from controllers import CategoryController

router = APIRouter()
@router.post("/addCategory")
async def post_category(cat:Category):
    return await CategoryController.addCategory(cat)

@router.get("/getAllCategories")
async def get_all_categories():
    return await CategoryController.getAllCategories()

