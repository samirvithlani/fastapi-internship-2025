from models.ProductModel import Product
from config.database import product_collection
from fastapi import APIRouter, HTTPException, UploadFile, File,Form
from fastapi.responses import JSONResponse
from bson import ObjectId
import shutil
import os


# Directory to save uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def create_product(product: Product):
    #convert category_id and sub_category_id,vendor_id to ObjectId
    print(product.dict())
    product.category_id = ObjectId(product.category_id)
    product.sub_category_id = ObjectId(product.sub_category_id)
    product.vendor_id = ObjectId(product.vendor_id)
    
    #insert product into database
    savedProduct= await product_collection.insert_one(product.dict())
    return JSONResponse(content={"message":"Product created successfully"},status_code=201)

async def create_Product_withFile(
    name: str = Form(...),
    price: float = Form(...),
    category_id: str = Form(...),
    sub_category_id: str = Form(...),
    vendor_id: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # Save the uploaded file
        file_ext = file.filename.split(".")[-1]  # Get file extension
        file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")  # Rename file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Create a product object
        product_data = {
            "name": name,
            "price": price,
            "category_id": ObjectId(category_id),
            "sub_category_id": ObjectId(sub_category_id),
            "vendor_id": ObjectId(vendor_id),
            "image_url": file_path  # Save file path in the database
        }
        return JSONResponse(
            content={
                "message": "Product created successfully",
                "image_url": file_path
            },
            status_code=201
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
