
from pydantic import BaseModel

from .grant import GrantOut


class GrantShowIn(BaseModel):
    data: GrantIn

class GrantShowOut(BaseModel):
    data: GrantOut

class GrantShowUpdate(BaseModel):
    data: GrantUpdate

class GrantShowDb(BaseModel):
    data: GrantDb

