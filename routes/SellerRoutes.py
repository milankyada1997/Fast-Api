from fastapi import APIRouter
from controllers import SellerController
from models.SellerModel import Seller, Sellerout

router = APIRouter()

@router.post("/seller")
async def post_seller(seller:Seller):
    return await SellerController.addSeller(seller)

@router.get("/sellers")
async def get_sellers():
    return await SellerController.getAllSellers()