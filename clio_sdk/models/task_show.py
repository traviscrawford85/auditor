from pydantic import BaseModel

from .task import TaskOut


class TaskShowIn(BaseModel):
    data: TaskIn

class TaskShowOut(BaseModel):
    data: TaskOut

class TaskShowUpdate(BaseModel):
    data: TaskUpdate

class TaskShowDb(BaseModel):
    data: TaskDb

