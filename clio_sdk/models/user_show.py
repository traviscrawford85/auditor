
from pydantic import BaseModel

from .user import UserOut


class UserShowIn(BaseModel):
    data: UserIn

class UserShowOut(BaseModel):
    data: UserOut

class UserShowUpdate(BaseModel):
    data: UserUpdate

class UserShowDb(BaseModel):
    data: UserDb

