from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillableclientBaseIn(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    name: Optional[str] = None
    billable_matters_count: Optional[int] = None

class BillableclientBaseOut(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    name: Optional[str] = None
    billable_matters_count: Optional[int] = None

class BillableclientBaseUpdate(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    name: Optional[str] = None
    billable_matters_count: Optional[int] = None

class BillableclientBaseDb(BaseModel):
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    name: Optional[str] = None
    billable_matters_count: Optional[int] = None

