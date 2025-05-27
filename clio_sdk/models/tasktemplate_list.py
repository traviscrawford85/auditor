from typing import List

from pydantic import BaseModel

from .tasktemplate import TasktemplateOut


class TasktemplateListIn(BaseModel):
    data: List[TasktemplateIn]

class TasktemplateListOut(BaseModel):
    data: List[TasktemplateOut]

class TasktemplateListUpdate(BaseModel):
    data: List[TasktemplateUpdate]

class TasktemplateListDb(BaseModel):
    data: List[TasktemplateDb]

