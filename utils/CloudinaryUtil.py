import cloudinary
from cloudinary.uploader import upload

#cloundinary configuration
cloudinary.config(
    cloud_name = "",
    api_key="",
    api_secret=""
)

#util functionn...

async def upload_image(image):
    result = upload(image)
    print("cloundianry response,",result)
    return result["secure_url"] #string
    
