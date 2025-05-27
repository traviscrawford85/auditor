from typing import List

from pydantic import BaseModel

from .group import GroupOut


class GroupListIn(BaseModel):
    data: List[GroupIn]

class GroupListOut(BaseModel):
    data: List[GroupOut]

class GroupListUpdate(BaseModel):
    data: List[GroupUpdate]

class GroupListDb(BaseModel):
    data: List[GroupDb]

