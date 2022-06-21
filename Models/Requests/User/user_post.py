from typing import Optional
import uuid
import bcrypt
from click import option
from pydantic import BaseModel, validator

class UserPost(BaseModel):
    id: Optional[str]
    email: str
    username: str 
    password: str

    @validator('id')
    def id_validator(cls):
        uuid_post = str(uuid.uuid4())
        return uuid_post

    @validator('password', pre=True)
    def password_validator(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(value.encode('utf-8'), salt).decode('utf-8')
        return password_hash