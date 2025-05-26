from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CurrencyListIn(BaseModel):
    data: List[Currency]

class CurrencyListOut(BaseModel):
    data: List[Currency]

class CurrencyListUpdate(BaseModel):
    data: List[Currency]

class CurrencyListDb(BaseModel):
    data: List[Currency]

