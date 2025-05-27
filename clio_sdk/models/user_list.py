from typing import List

from pydantic import BaseModel

from .user import UserOut


class UserListIn(BaseModel):
    data: List[UserIn]

class UserListOut(BaseModel):
    data: List[UserOut]

class UserListUpdate(BaseModel):
    data: List[UserUpdate]

class UserListDb(BaseModel):
    data: List[UserDb]

