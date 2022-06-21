from fastapi import APIRouter, Response
from Models.Requests.User.user_patch import UserPatch
from Models.Requests.User.user_post import UserPost
from Models.user_model import UserModel
from Repositories.user_repository import UserRepository

router = APIRouter()

@router.get("/")
async def get_all_users():
    return await UserModel.objects.all()

@router.get("/{id}")
async def get_user(id: int, response: Response):
    response_user = await UserRepository.UserGetById(id)
    response.status_code = response_user["status"] 
    return response_user

@router.post("/")
async def post_user(create_user: UserPost, response: Response):
    response_user = await UserRepository.UserPost(create_user)
    response.status_code = response_user["status"]
    return response_user

@router.patch("/{id}")
async def patch_user(props_patch: UserPatch, id: int, response: Response):
    response_user = await UserRepository.UserPatch(props_patch, id)
    response.status_code = response_user["status"]
    return response_user

