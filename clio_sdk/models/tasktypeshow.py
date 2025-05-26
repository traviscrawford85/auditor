from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktypeShowIn(BaseModel):
    data: Tasktype

class TasktypeShowOut(BaseModel):
    data: Tasktype

class TasktypeShowUpdate(BaseModel):
    data: Tasktype

class TasktypeShowDb(BaseModel):
    data: Tasktype

