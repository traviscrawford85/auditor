from typing import Optional

from pydantic import BaseModel


class BillableclientBaseIn(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

class BillableclientBaseOut(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

class BillableclientBaseUpdate(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

class BillableclientBaseDb(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

