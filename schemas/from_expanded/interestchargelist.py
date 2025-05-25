from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class InterestchargeListIn(BaseModel):
    data: List[Any]

class InterestchargeListOut(BaseModel):
    data: List[Any]

class InterestchargeListUpdate(BaseModel):
    data: List[Any]

class InterestchargeListDb(BaseModel):
    data: List[Any]

