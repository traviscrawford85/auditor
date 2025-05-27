
from pydantic import BaseModel

from .group import GroupOut


class GroupShowIn(BaseModel):
    data: GroupIn

class GroupShowOut(BaseModel):
    data: GroupOut

class GroupShowUpdate(BaseModel):
    data: GroupUpdate

class GroupShowDb(BaseModel):
    data: GroupDb

