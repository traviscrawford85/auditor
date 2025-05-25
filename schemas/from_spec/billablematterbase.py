from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillablematterbaseIn(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

class BillablematterbaseOut(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

class BillablematterbaseUpdate(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

class BillablematterbaseDb(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

