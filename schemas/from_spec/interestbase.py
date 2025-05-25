from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class InterestbaseIn(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestbaseOut(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestbaseUpdate(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestbaseDb(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

