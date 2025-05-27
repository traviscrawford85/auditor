from typing import List

from pydantic import BaseModel

from .banktransaction import BanktransactionOut


class BanktransactionListIn(BaseModel):
    data: List[BanktransactionIn]

class BanktransactionListOut(BaseModel):
    data: List[BanktransactionOut]

class BanktransactionListUpdate(BaseModel):
    data: List[BanktransactionUpdate]

class BanktransactionListDb(BaseModel):
    data: List[BanktransactionDb]

