from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BankaccountShowIn(BaseModel):
    data: Bankaccount

class BankaccountShowOut(BaseModel):
    data: Bankaccount

class BankaccountShowUpdate(BaseModel):
    data: Bankaccount

class BankaccountShowDb(BaseModel):
    data: Bankaccount

