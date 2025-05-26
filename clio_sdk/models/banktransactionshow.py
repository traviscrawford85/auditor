from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransactionShowIn(BaseModel):
    data: Banktransaction

class BanktransactionShowOut(BaseModel):
    data: Banktransaction

class BanktransactionShowUpdate(BaseModel):
    data: Banktransaction

class BanktransactionShowDb(BaseModel):
    data: Banktransaction

