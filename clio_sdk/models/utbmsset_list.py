from typing import List

from pydantic import BaseModel

from .utbmsset import UtbmssetOut


class UtbmssetListIn(BaseModel):
    data: List[UtbmssetIn]

class UtbmssetListOut(BaseModel):
    data: List[UtbmssetOut]

class UtbmssetListUpdate(BaseModel):
    data: List[UtbmssetUpdate]

class UtbmssetListDb(BaseModel):
    data: List[UtbmssetDb]

