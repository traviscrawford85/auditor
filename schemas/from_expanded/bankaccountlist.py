from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BankaccountListIn(BaseModel):
    data: List[Any]

class BankaccountListOut(BaseModel):
    data: List[Any]

class BankaccountListUpdate(BaseModel):
    data: List[Any]

class BankaccountListDb(BaseModel):
    data: List[Any]

