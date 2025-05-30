from typing import Optional

from pydantic import BaseModel


class InterestIn(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestOut(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestUpdate(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

class InterestDb(BaseModel):
    balance: Optional[str] = None
    period: Optional[str] = None
    rate: Optional[str] = None
    total: Optional[str] = None
    type: Optional[str] = None

