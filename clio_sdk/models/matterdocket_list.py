from typing import List

from pydantic import BaseModel

from .matterdocket import MatterdocketOut


class MatterdocketListIn(BaseModel):
    data: List[MatterdocketIn]

class MatterdocketListOut(BaseModel):
    data: List[MatterdocketOut]

class MatterdocketListUpdate(BaseModel):
    data: List[MatterdocketUpdate]

class MatterdocketListDb(BaseModel):
    data: List[MatterdocketDb]

