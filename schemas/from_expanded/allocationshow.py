from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AllocationShowIn(BaseModel):
    data: Any

class AllocationShowOut(BaseModel):
    data: Any

class AllocationShowUpdate(BaseModel):
    data: Any

class AllocationShowDb(BaseModel):
    data: Any

