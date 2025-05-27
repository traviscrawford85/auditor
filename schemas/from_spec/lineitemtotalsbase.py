from typing import Optional

from pydantic import BaseModel


class LineitemtotalsBaseIn(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

class LineitemtotalsBaseOut(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

class LineitemtotalsBaseUpdate(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

class LineitemtotalsBaseDb(BaseModel):
    quantity: Optional[str] = None
    price: Optional[str] = None
    discount_percent: Optional[str] = None
    total: Optional[str] = None
    sub_total: Optional[str] = None

