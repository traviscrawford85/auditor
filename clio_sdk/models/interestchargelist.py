from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class InterestchargeListIn(BaseModel):
    data: List[Interestcharge]

class InterestchargeListOut(BaseModel):
    data: List[Interestcharge]

class InterestchargeListUpdate(BaseModel):
    data: List[Interestcharge]

class InterestchargeListDb(BaseModel):
    data: List[Interestcharge]

