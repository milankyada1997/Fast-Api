from models.SellerModel import Seller, Sellerout
from bson import ObjectId
from config.database import seller_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt

async def addSeller(seller:Seller):
    result = await seller_collection.insert_one(seller.dict())
    return JSONResponse(content={"message":"Seller added successfully"},status_code=201)

async def getAllSellers():
    Sellers = await seller_collection.find().to_list(length=None)
    print("sellers",Sellers)
    return [Sellerout(**seller)for seller in Sellers]
