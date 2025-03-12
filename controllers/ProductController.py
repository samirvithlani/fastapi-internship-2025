from models.ProductModel import Product,ProductOut
from config.database import product_collection,category_collection,user_collection,sub_category_collection
from fastapi import APIRouter, HTTPException, UploadFile, File,Form
from fastapi.responses import JSONResponse
from bson import ObjectId
import shutil
import os
from utils.CloudinaryUtil import upload_image


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
    image: UploadFile = File(...)
):
    try:
    
        # Ensure upload directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        #abc.jpg -> ["abc", "jpg"]
        # Save the uploaded file
        file_ext = image.filename.split(".")[-1]  # Get file extension
        file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")  # Rename file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        # Create a product object (DO NOT include `image` directly)
        
        #upload image to cloudinary
        image_url = await upload_image(file_path)
        
        product_data = {
            "name": name,
            "price": price,
            "category_id": str(ObjectId(category_id)),
            "sub_category_id": str(ObjectId(sub_category_id)),
            "vendor_id": str(ObjectId(vendor_id)),
            "image_url":image_url # Only store path, NOT file object
        }
        print(product_data)
        insertedProduct = await product_collection.insert_one(product_data)

        return JSONResponse(content={"message": "Product created successfully"}, status_code=201)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



async def get_products():
    try:
        products = await product_collection.find().to_list(None)  # Fetch all products

        def convert_objectid_to_str(data):
            """Recursively converts ObjectId fields to strings."""
            if isinstance(data, ObjectId):
                return str(data)
            elif isinstance(data, dict):
                return {k: convert_objectid_to_str(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [convert_objectid_to_str(i) for i in data]
            return data

        for prod in products:
            # Convert all ObjectId fields in product, category, sub_category, and vendor
            prod["_id"] = str(prod["_id"])
            prod["category_id"] = str(prod["category_id"])
            prod["sub_category_id"] = str(prod["sub_category_id"])
            prod["vendor_id"] = str(prod["vendor_id"])

            category = await category_collection.find_one({"_id": ObjectId(prod["category_id"])})
            if category:
                prod["category"] = convert_objectid_to_str(category)

            sub_category = await sub_category_collection.find_one({"_id": ObjectId(prod["sub_category_id"])})
            if sub_category:
                prod["sub_category"] = convert_objectid_to_str(sub_category)

            vendor = await user_collection.find_one({"_id": ObjectId(prod["vendor_id"])})
            if vendor:
                prod["vendor"] = convert_objectid_to_str(vendor)  # Convert vendor fields

        return [ProductOut(**product) for product in products]

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching products")
