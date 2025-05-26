from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransactionListIn(BaseModel):
    data: List[Banktransaction]

class BanktransactionListOut(BaseModel):
    data: List[Banktransaction]

class BanktransactionListUpdate(BaseModel):
    data: List[Banktransaction]

class BanktransactionListDb(BaseModel):
    data: List[Banktransaction]

