from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DiscountbaseIn(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

class DiscountbaseOut(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

class DiscountbaseUpdate(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

class DiscountbaseDb(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    note: Optional[str] = None
    early_payment_rate: Optional[str] = None
    early_payment_period: Optional[str] = None

