from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskShowIn(BaseModel):
    data: Task

class TaskShowOut(BaseModel):
    data: Task

class TaskShowUpdate(BaseModel):
    data: Task

class TaskShowDb(BaseModel):
    data: Task

