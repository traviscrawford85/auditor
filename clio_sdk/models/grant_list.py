from typing import List

from pydantic import BaseModel

from .grant import GrantOut


class GrantListIn(BaseModel):
    data: List[GrantIn]

class GrantListOut(BaseModel):
    data: List[GrantOut]

class GrantListUpdate(BaseModel):
    data: List[GrantUpdate]

class GrantListDb(BaseModel):
    data: List[GrantDb]

