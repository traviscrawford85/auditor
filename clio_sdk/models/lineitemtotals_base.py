from typing import Optional

from pydantic import BaseModel


class LineitemtotalsBaseIn(BaseModel):
    quantity: Optional[float] = None
    price: Optional[float] = None
    discount_percent: Optional[float] = None
    total: Optional[float] = None
    sub_total: Optional[float] = None

class LineitemtotalsBaseOut(BaseModel):
    quantity: Optional[float] = None
    price: Optional[float] = None
    discount_percent: Optional[float] = None
    total: Optional[float] = None
    sub_total: Optional[float] = None

class LineitemtotalsBaseUpdate(BaseModel):
    quantity: Optional[float] = None
    price: Optional[float] = None
    discount_percent: Optional[float] = None
    total: Optional[float] = None
    sub_total: Optional[float] = None

class LineitemtotalsBaseDb(BaseModel):
    quantity: Optional[float] = None
    price: Optional[float] = None
    discount_percent: Optional[float] = None
    total: Optional[float] = None
    sub_total: Optional[float] = None

