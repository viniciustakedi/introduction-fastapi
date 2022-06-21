from uuid import uuid4
import ormar
import re
from pydantic import validator
from config import database, metadata

class UserModel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "users"

    id: int = ormar.String(primary_key=True, max_length=36)
    email: str = ormar.String(max_length=155, unique=True)
    username: str = ormar.String(max_length=255)
    password: str = ormar.String(max_length=255)

    @validator('email')
    def email_validator(cls, value): #cls = classed, value = value
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid Email")
        return value