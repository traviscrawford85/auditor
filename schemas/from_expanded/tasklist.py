from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskListIn(BaseModel):
    data: List[Any]

class TaskListOut(BaseModel):
    data: List[Any]

class TaskListUpdate(BaseModel):
    data: List[Any]

class TaskListDb(BaseModel):
    data: List[Any]

