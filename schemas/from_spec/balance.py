from typing import Optional

from pydantic import BaseModel


class BalanceIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalanceOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalanceUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalanceDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

