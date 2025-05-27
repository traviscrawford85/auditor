
from pydantic import BaseModel

from .grantfundingsource import GrantfundingsourceOut


class GrantfundingsourceShowIn(BaseModel):
    data: GrantfundingsourceIn

class GrantfundingsourceShowOut(BaseModel):
    data: GrantfundingsourceOut

class GrantfundingsourceShowUpdate(BaseModel):
    data: GrantfundingsourceUpdate

class GrantfundingsourceShowDb(BaseModel):
    data: GrantfundingsourceDb

