from typing import Optional

from pydantic import BaseModel


class InterestBaseIn(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestBaseOut(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestBaseUpdate(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestBaseDb(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

