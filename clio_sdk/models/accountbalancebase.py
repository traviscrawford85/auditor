from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AccountbalanceBaseIn(BaseModel):
    id: Optional[int] = None
    balance: Optional[float] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalanceBaseOut(BaseModel):
    id: Optional[int] = None
    balance: Optional[float] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalanceBaseUpdate(BaseModel):
    id: Optional[int] = None
    balance: Optional[float] = None
    type: Optional[str] = None
    name: Optional[str] = None

class AccountbalanceBaseDb(BaseModel):
    id: Optional[int] = None
    balance: Optional[float] = None
    type: Optional[str] = None
    name: Optional[str] = None

