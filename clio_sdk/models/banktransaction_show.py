
from pydantic import BaseModel

from .banktransaction import BanktransactionOut


class BanktransactionShowIn(BaseModel):
    data: BanktransactionIn

class BanktransactionShowOut(BaseModel):
    data: BanktransactionOut

class BanktransactionShowUpdate(BaseModel):
    data: BanktransactionUpdate

class BanktransactionShowDb(BaseModel):
    data: BanktransactionDb

