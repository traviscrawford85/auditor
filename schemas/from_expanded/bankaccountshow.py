from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BankaccountShowIn(BaseModel):
    data: Any

class BankaccountShowOut(BaseModel):
    data: Any

class BankaccountShowUpdate(BaseModel):
    data: Any

class BankaccountShowDb(BaseModel):
    data: Any

