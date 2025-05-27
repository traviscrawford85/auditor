from typing import List

from pydantic import BaseModel

from .allocation import AllocationOut


class AllocationListIn(BaseModel):
    data: List[AllocationIn]

class AllocationListOut(BaseModel):
    data: List[AllocationOut]

class AllocationListUpdate(BaseModel):
    data: List[AllocationUpdate]

class AllocationListDb(BaseModel):
    data: List[AllocationDb]

