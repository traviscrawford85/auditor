from typing import Optional

from pydantic import BaseModel


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

