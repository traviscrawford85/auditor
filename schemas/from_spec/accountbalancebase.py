from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AccountbalanceBaseIn(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalanceBaseOut(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalanceBaseUpdate(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalanceBaseDb(BaseModel):
    id: Optional[str] = None
    balance: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

