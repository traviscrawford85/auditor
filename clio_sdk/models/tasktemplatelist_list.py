from typing import List

from pydantic import BaseModel

from .tasktemplatelist import TasktemplatelistOut


class TasktemplatelistListIn(BaseModel):
    data: List[TasktemplatelistIn]

class TasktemplatelistListOut(BaseModel):
    data: List[TasktemplatelistOut]

class TasktemplatelistListUpdate(BaseModel):
    data: List[TasktemplatelistUpdate]

class TasktemplatelistListDb(BaseModel):
    data: List[TasktemplatelistDb]

