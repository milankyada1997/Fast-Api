from pydantic import BaseModel,Field,validator
from bson import ObjectId
import bcrypt
from typing import Optional, Dict, Any

class seller(BaseModel):
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