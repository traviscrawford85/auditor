from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskListIn(BaseModel):
    data: List[Task]

class TaskListOut(BaseModel):
    data: List[Task]

class TaskListUpdate(BaseModel):
    data: List[Task]

class TaskListDb(BaseModel):
    data: List[Task]

