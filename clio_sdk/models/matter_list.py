from typing import List

from pydantic import BaseModel

from .matter import MatterOut


class MatterListIn(BaseModel):
    data: List[MatterIn]

class MatterListOut(BaseModel):
    data: List[MatterOut]

class MatterListUpdate(BaseModel):
    data: List[MatterUpdate]

class MatterListDb(BaseModel):
    data: List[MatterDb]

