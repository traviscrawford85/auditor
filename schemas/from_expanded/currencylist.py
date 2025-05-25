from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CurrencyListIn(BaseModel):
    data: List[Any]

class CurrencyListOut(BaseModel):
    data: List[Any]

class CurrencyListUpdate(BaseModel):
    data: List[Any]

class CurrencyListDb(BaseModel):
    data: List[Any]

