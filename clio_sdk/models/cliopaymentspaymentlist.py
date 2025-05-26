from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentspaymentListIn(BaseModel):
    data: List[Cliopaymentspayment]

class CliopaymentspaymentListOut(BaseModel):
    data: List[Cliopaymentspayment]

class CliopaymentspaymentListUpdate(BaseModel):
    data: List[Cliopaymentspayment]

class CliopaymentspaymentListDb(BaseModel):
    data: List[Cliopaymentspayment]

