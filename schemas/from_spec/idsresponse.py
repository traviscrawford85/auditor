from typing import List

from pydantic import BaseModel


class IdsresponseIn(BaseModel):
    data: List[int]

class IdsresponseOut(BaseModel):
    data: List[int]

class IdsresponseUpdate(BaseModel):
    data: List[int]

class IdsresponseDb(BaseModel):
    data: List[int]

