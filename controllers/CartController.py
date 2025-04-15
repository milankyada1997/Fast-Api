from models.CartModel import CartItem
from fastapi import APIRouter, HTTPException, Request
from config.database import cart_collection,product_collection
from bson import ObjectId
from models.ProductModel import ProductOut

cart_router = APIRouter()

@cart_router.post("/add_to_cart/")
async def add_to_cart(cart_item: CartItem):
    try:
        cart_data = {
            "user_id": ObjectId(cart_item.user_id),
            "product_id": ObjectId(cart_item.product_id),
        }
        await cart_collection.insert_one(cart_data)
        return {"message": "Item added to cart"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@cart_router.get("/get_cart_items/{user_id}")
async def get_cart_items(user_id: str):
    try:
        cart_items = await cart_collection.find({"user_id": ObjectId(user_id)}).to_list(None)

        result = []
        for item in cart_items:
            product = await product_collection.find_one({"_id": ObjectId(item["product_id"])})
            if product:
                product["_id"] = str(product["_id"])
                product["category_id"] = str(product["category_id"])
                product["sub_category_id"] = str(product["sub_category_id"])
                product["seller_id"] = str(product["seller_id"])

                result.append({
                    "product": product
                })

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch cart items: {str(e)}")
    
@cart_router.delete("/remove_from_cart/")
async def remove_from_cart(request: Request):
    try:
        body = await request.json()
        user_id = body.get("user_id")
        product_id = body.get("product_id")

        if not user_id or not product_id:
            raise HTTPException(status_code=400, detail="Missing user_id or product_id")

        result = await cart_collection.delete_one({
            "user_id": ObjectId(user_id),
            "product_id": ObjectId(product_id)
        })

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Cart item not found")

        return {"message": "Item removed from cart"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

