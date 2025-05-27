from typing import List

from pydantic import BaseModel

from .task import TaskOut


class TaskListIn(BaseModel):
    data: List[TaskIn]

class TaskListOut(BaseModel):
    data: List[TaskOut]

class TaskListUpdate(BaseModel):
    data: List[TaskUpdate]

class TaskListDb(BaseModel):
    data: List[TaskDb]

