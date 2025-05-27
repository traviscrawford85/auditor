from typing import List

from pydantic import BaseModel

from .customaction import CustomactionOut


class CustomactionListIn(BaseModel):
    data: List[CustomactionIn]

class CustomactionListOut(BaseModel):
    data: List[CustomactionOut]

class CustomactionListUpdate(BaseModel):
    data: List[CustomactionUpdate]

class CustomactionListDb(BaseModel):
    data: List[CustomactionDb]

