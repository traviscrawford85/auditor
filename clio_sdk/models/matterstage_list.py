from typing import List

from pydantic import BaseModel

from .matterstage import MatterstageOut


class MatterstageListIn(BaseModel):
    data: List[MatterstageIn]

class MatterstageListOut(BaseModel):
    data: List[MatterstageOut]

class MatterstageListUpdate(BaseModel):
    data: List[MatterstageUpdate]

class MatterstageListDb(BaseModel):
    data: List[MatterstageDb]

