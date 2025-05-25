from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillableclientbaseIn(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

class BillableclientbaseOut(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

class BillableclientbaseUpdate(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

class BillableclientbaseDb(BaseModel):
    id: Optional[str] = None
    unbilled_hours: Optional[str] = None
    unbilled_amount: Optional[str] = None
    amount_in_trust: Optional[str] = None
    name: Optional[str] = None
    billable_matters_count: Optional[str] = None

