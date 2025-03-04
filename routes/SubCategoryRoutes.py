from fastapi import APIRouter
from models.SubCategoryModel import SubCategory
from controllers import SubCategoryController

router = APIRouter()
@router.post("/addSubCategory")
async def post_sub_category(sub_cat:SubCategory):
    return await SubCategoryController.addSubCategory(sub_cat)

@router.get("/getAllSubCategories")
async def get_all_sub_categories():
    return await SubCategoryController.getAllSubCategories()