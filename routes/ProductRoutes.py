from fastapi import APIRouter, HTTPException
from models.ProductModel import Product
from fastapi import APIRouter, Form, UploadFile, File
from controllers import ProductController

router = APIRouter()

@router.post("/create_product")
async def create_product(product: Product):
    print(product)
    return await ProductController.create_product(product)

@router.post("/create_product_file")
async def create_product(name: str = Form(...),
    price: float = Form(...),
    category_id: str = Form(...),
    sub_category_id: str = Form(...),
    vendor_id: str = Form(...),
    image: UploadFile = File(...)):
    #print(product)
     return await ProductController.create_Product_withFile(
        name, price, category_id, sub_category_id, vendor_id, image
    )
     
@router.get("/get_products")
async def get_products():
    return await ProductController.get_products()     