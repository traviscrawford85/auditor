from typing import Optional

from pydantic import BaseModel


class BillablematterBaseIn(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

class BillablematterBaseOut(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

class BillablematterBaseUpdate(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

class BillablematterBaseDb(BaseModel):
    currency_code: Optional[str] = None
    currency_id: Optional[str] = None
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    display_number: Optional[str] = None

