from typing import Optional

from pydantic import BaseModel


class InterestBaseIn(BaseModel):
    balance: Optional[float] = None
    period: Optional[int] = None
    rate: Optional[float] = None
    total: Optional[float] = None
    type: Optional[str] = None

class InterestBaseOut(BaseModel):
    balance: Optional[float] = None
    period: Optional[int] = None
    rate: Optional[float] = None
    total: Optional[float] = None
    type: Optional[str] = None

class InterestBaseUpdate(BaseModel):
    balance: Optional[float] = None
    period: Optional[int] = None
    rate: Optional[float] = None
    total: Optional[float] = None
    type: Optional[str] = None

class InterestBaseDb(BaseModel):
    balance: Optional[float] = None
    period: Optional[int] = None
    rate: Optional[float] = None
    total: Optional[float] = None
    type: Optional[str] = None

