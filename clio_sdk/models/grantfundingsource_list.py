from typing import List

from pydantic import BaseModel

from .grantfundingsource import GrantfundingsourceOut


class GrantfundingsourceListIn(BaseModel):
    data: List[GrantfundingsourceIn]

class GrantfundingsourceListOut(BaseModel):
    data: List[GrantfundingsourceOut]

class GrantfundingsourceListUpdate(BaseModel):
    data: List[GrantfundingsourceUpdate]

class GrantfundingsourceListDb(BaseModel):
    data: List[GrantfundingsourceDb]

