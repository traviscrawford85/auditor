from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransactionListIn(BaseModel):
    data: List[Any]

class BanktransactionListOut(BaseModel):
    data: List[Any]

class BanktransactionListUpdate(BaseModel):
    data: List[Any]

class BanktransactionListDb(BaseModel):
    data: List[Any]

