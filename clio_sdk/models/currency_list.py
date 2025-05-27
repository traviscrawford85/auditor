from typing import List

from pydantic import BaseModel

from .currency import CurrencyOut


class CurrencyListIn(BaseModel):
    data: List[CurrencyIn]

class CurrencyListOut(BaseModel):
    data: List[CurrencyOut]

class CurrencyListUpdate(BaseModel):
    data: List[CurrencyUpdate]

class CurrencyListDb(BaseModel):
    data: List[CurrencyDb]

