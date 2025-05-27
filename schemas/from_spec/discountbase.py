from typing import Optional

from pydantic import BaseModel


class DiscountBaseIn(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

class DiscountBaseOut(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

class DiscountBaseUpdate(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

class DiscountBaseDb(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

