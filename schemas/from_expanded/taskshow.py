from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TaskShowIn(BaseModel):
    data: Any

class TaskShowOut(BaseModel):
    data: Any

class TaskShowUpdate(BaseModel):
    data: Any

class TaskShowDb(BaseModel):
    data: Any

