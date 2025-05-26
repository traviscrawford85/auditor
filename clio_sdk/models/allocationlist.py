from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AllocationListIn(BaseModel):
    data: List[Allocation]

class AllocationListOut(BaseModel):
    data: List[Allocation]

class AllocationListUpdate(BaseModel):
    data: List[Allocation]

class AllocationListDb(BaseModel):
    data: List[Allocation]

