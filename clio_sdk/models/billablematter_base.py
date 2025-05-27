from typing import Optional

from pydantic import BaseModel


class BillablematterBaseIn(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

class BillablematterBaseOut(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

class BillablematterBaseUpdate(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

class BillablematterBaseDb(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

