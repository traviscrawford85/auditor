from typing import Optional

from pydantic import BaseModel


class BalanceBaseIn(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalanceBaseOut(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalanceBaseUpdate(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

class BalanceBaseDb(BaseModel):
    id: Optional[str] = None
    amount: Optional[str] = None
    type: Optional[str] = None
    interest_amount: Optional[str] = None
    due: Optional[str] = None

