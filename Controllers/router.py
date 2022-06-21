from fastapi import APIRouter
from Controllers import user_controller as user

router = APIRouter()

router.include_router(user.router, prefix="/user", tags=["user"])