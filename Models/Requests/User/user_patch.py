from typing import List, Optional
from pydantic import BaseModel

class UserPatch(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None