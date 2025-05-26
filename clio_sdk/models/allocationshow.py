from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AllocationShowIn(BaseModel):
    data: Allocation

class AllocationShowOut(BaseModel):
    data: Allocation

class AllocationShowUpdate(BaseModel):
    data: Allocation

class AllocationShowDb(BaseModel):
    data: Allocation

