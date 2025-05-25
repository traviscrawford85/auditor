from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentspaymentListIn(BaseModel):
    data: List[Any]

class CliopaymentspaymentListOut(BaseModel):
    data: List[Any]

class CliopaymentspaymentListUpdate(BaseModel):
    data: List[Any]

class CliopaymentspaymentListDb(BaseModel):
    data: List[Any]

