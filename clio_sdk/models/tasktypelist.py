from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktypeListIn(BaseModel):
    data: List[Tasktype]

class TasktypeListOut(BaseModel):
    data: List[Tasktype]

class TasktypeListUpdate(BaseModel):
    data: List[Tasktype]

class TasktypeListDb(BaseModel):
    data: List[Tasktype]

