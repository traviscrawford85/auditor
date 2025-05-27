
from pydantic import BaseModel

from .tasktemplate import TasktemplateOut


class TasktemplateShowIn(BaseModel):
    data: TasktemplateIn

class TasktemplateShowOut(BaseModel):
    data: TasktemplateOut

class TasktemplateShowUpdate(BaseModel):
    data: TasktemplateUpdate

class TasktemplateShowDb(BaseModel):
    data: TasktemplateDb

