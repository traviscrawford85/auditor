
from pydantic import BaseModel

from .lineitem import LineitemOut


class LineitemShowIn(BaseModel):
    data: LineitemIn

class LineitemShowOut(BaseModel):
    data: LineitemOut

class LineitemShowUpdate(BaseModel):
    data: LineitemUpdate

class LineitemShowDb(BaseModel):
    data: LineitemDb

