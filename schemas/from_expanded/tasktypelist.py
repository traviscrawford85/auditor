from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktypeListIn(BaseModel):
    data: List[Any]

class TasktypeListOut(BaseModel):
    data: List[Any]

class TasktypeListUpdate(BaseModel):
    data: List[Any]

class TasktypeListDb(BaseModel):
    data: List[Any]

