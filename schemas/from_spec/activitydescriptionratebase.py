from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitydescriptionratebaseIn(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionratebaseOut(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionratebaseUpdate(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionratebaseDb(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

