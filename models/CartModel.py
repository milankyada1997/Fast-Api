from pydantic import BaseModel

class CartItem(BaseModel):
    user_id: str
    product_id: str
