from typing import List

from pydantic import BaseModel

from .tasktype_base import TasktypeOut


class TasktypeListIn(BaseModel):
    data: List[TasktypeIn]

class TasktypeListOut(BaseModel):
    data: List[TasktypeOut]

class TasktypeListUpdate(BaseModel):
    data: List[TasktypeUpdate]

class TasktypeListDb(BaseModel):
    data: List[TasktypeDb]

