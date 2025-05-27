
from pydantic import BaseModel

from .matterdocket import MatterdocketOut


class MatterdocketShowIn(BaseModel):
    data: MatterdocketIn

class MatterdocketShowOut(BaseModel):
    data: MatterdocketOut

class MatterdocketShowUpdate(BaseModel):
    data: MatterdocketUpdate

class MatterdocketShowDb(BaseModel):
    data: MatterdocketDb

