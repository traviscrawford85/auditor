from typing import List

from pydantic import BaseModel

from .lineitem import LineitemOut


class LineitemListIn(BaseModel):
    data: List[LineitemIn]

class LineitemListOut(BaseModel):
    data: List[LineitemOut]

class LineitemListUpdate(BaseModel):
    data: List[LineitemUpdate]

class LineitemListDb(BaseModel):
    data: List[LineitemDb]

