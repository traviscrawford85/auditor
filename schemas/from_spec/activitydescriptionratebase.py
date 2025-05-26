from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitydescriptionrateBaseIn(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionrateBaseOut(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionrateBaseUpdate(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionrateBaseDb(BaseModel):
    amount: Optional[str] = None
    non_billable_amount: Optional[str] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

