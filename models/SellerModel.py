from pydantic import BaseModel,Field,validator
from bson import ObjectId
import bcrypt
from typing import Optional, Dict, Any

class Seller(BaseModel):

#     seller_id
#    full_name
#    business_name
#    business_email
#    phone
#    password
#   business_address
#    gst id
#       bank_account
#   store_logo
#    government_id
#   verified_status
#   time in & out
#   store_name

    fullName:str
    businessName:str
    businessEmail:str
    password:str
    businessAddress:str
    gstId:str
    bankAccount:str
    phone:str

    @validator("password", pre=True, always=True)
    def encrypt_password(cls, v):
        if v is None:
            return None
        return bcrypt.hashpw(v.encode("utf-8"),bcrypt.gensalt())

class Sellerout(Seller):
    id:str = Field(alias="_id")

    @validator("id",pre=True,always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v

