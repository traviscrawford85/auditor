from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BalancebaseIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalancebaseOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalancebaseUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalancebaseDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

