from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemtotalsbaseIn(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

class LineitemtotalsbaseOut(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

class LineitemtotalsbaseUpdate(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

class LineitemtotalsbaseDb(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

