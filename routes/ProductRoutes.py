from fastapi import APIRouter, HTTPException
from models.ProductModel import Product
from controllers import ProductController

router = APIRouter()

@router.post("/create_product")
async def create_product(product: Product):
    print(product)
    return await ProductController.create_product(product)