from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AllocationListIn(BaseModel):
    data: List[Any]

class AllocationListOut(BaseModel):
    data: List[Any]

class AllocationListUpdate(BaseModel):
    data: List[Any]

class AllocationListDb(BaseModel):
    data: List[Any]

