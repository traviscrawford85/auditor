from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillablematterBaseIn(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[int] = None
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

class BillablematterBaseOut(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[int] = None
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

class BillablematterBaseUpdate(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[int] = None
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

class BillablematterBaseDb(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[int] = None
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

