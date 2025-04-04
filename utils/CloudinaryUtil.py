import cloudinary
from cloudinary.uploader import upload

cloudinary.config(
    cloud_name = "dd6pitmvp",
    api_key="add your api secrect keuy",
    api_secret="add your clodinary pass key"
)

#util functionn...

async def upload_image(image):
    result = upload(image)
    print("cloundianry response,",result)
    return result["secure_url"] #string
    
