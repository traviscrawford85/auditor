from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AccountbalancebaseIn(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalancebaseOut(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalancebaseUpdate(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalancebaseDb(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

