from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DiscountBaseIn(BaseModel):
    rate: Optional[float] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[int] = None
    early_payment_period: Optional[int] = None

class DiscountBaseOut(BaseModel):
    rate: Optional[float] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[int] = None
    early_payment_period: Optional[int] = None

class DiscountBaseUpdate(BaseModel):
    rate: Optional[float] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[int] = None
    early_payment_period: Optional[int] = None

class DiscountBaseDb(BaseModel):
    rate: Optional[float] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[int] = None
    early_payment_period: Optional[int] = None

