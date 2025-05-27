
from pydantic import BaseModel

from .tasktype import TasktypeOut


class TasktypeShowIn(BaseModel):
    data: TasktypeIn

class TasktypeShowOut(BaseModel):
    data: TasktypeOut

class TasktypeShowUpdate(BaseModel):
    data: TasktypeUpdate

class TasktypeShowDb(BaseModel):
    data: TasktypeDb

