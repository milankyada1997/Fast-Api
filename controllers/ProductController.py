from models.ProductModel import Product
from config.database import product_collection
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse  
from bson import ObjectId

async def create_product(product: Product):
    print(product.dict())
    product.category_id = ObjectId(product.category_id)
    product.sub_category_id = ObjectId(product.sub_category_id)
    product.seller_id = ObjectId(product.seller_id)

    savedProduct = await product_collection.insert_one(product.dict())
    return JSONResponse(content={"message": "Product created successfully"}, status_code=201)