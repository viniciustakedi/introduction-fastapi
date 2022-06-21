from json import dumps, loads
from pydantic import validator
from Models.user_model import UserModel
import ormar

class UserRepository:
    async def UserGetById(id, status_code=200):
        try:
            user = await UserModel.objects.get(id=id)
            return {"status": status_code, "data": user}
        except ormar.exceptions.NoMatch:
            status_code = 404
            return {"status": status_code, "message": "User not found"}
    
    async def UserPost(user, status_code=201):
            attributes = user.dict(exclude_unset=True)
            user_add = UserModel(**attributes)
            await user_add.save()
            return {"status": status_code, "message": "User created", "data": user} 
    
    async def UserPatch(props_patch, id, status_code=200):
            try:
                user = await UserModel.objects.get(id=id)
                props_updated = props_patch.dict(exclude_unset=True)
                await user.update(**props_updated)
                return {"status": status_code, "message": "User updated", "data": user}
            except ormar.exceptions.NoMatch:
                status_code = 404
                return {"status": status_code, "message": "User not found"}