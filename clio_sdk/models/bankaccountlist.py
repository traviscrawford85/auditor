from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BankaccountListIn(BaseModel):
    data: List[Bankaccount]

class BankaccountListOut(BaseModel):
    data: List[Bankaccount]

class BankaccountListUpdate(BaseModel):
    data: List[Bankaccount]

class BankaccountListDb(BaseModel):
    data: List[Bankaccount]

