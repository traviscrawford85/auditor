from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BalanceBaseIn(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    interest_amount: Optional[float] = None
    due: Optional[float] = None

class BalanceBaseOut(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    interest_amount: Optional[float] = None
    due: Optional[float] = None

class BalanceBaseUpdate(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    interest_amount: Optional[float] = None
    due: Optional[float] = None

class BalanceBaseDb(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    interest_amount: Optional[float] = None
    due: Optional[float] = None

