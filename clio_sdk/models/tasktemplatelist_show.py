
from pydantic import BaseModel

from .tasktemplatelist import TasktemplatelistOut


class TasktemplatelistShowIn(BaseModel):
    data: TasktemplatelistIn

class TasktemplatelistShowOut(BaseModel):
    data: TasktemplatelistOut

class TasktemplatelistShowUpdate(BaseModel):
    data: TasktemplatelistUpdate

class TasktemplatelistShowDb(BaseModel):
    data: TasktemplatelistDb

