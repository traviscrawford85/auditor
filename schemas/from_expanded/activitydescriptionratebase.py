from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitydescriptionrateBaseIn(BaseModel):
    amount: Optional[float] = None
    non_billable_amount: Optional[float] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionrateBaseOut(BaseModel):
    amount: Optional[float] = None
    non_billable_amount: Optional[float] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionrateBaseUpdate(BaseModel):
    amount: Optional[float] = None
    non_billable_amount: Optional[float] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

class ActivitydescriptionrateBaseDb(BaseModel):
    amount: Optional[float] = None
    non_billable_amount: Optional[float] = None
    type: Optional[str] = None
    hierarchy: Optional[str] = None

