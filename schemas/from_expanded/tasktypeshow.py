from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktypeShowIn(BaseModel):
    data: Any

class TasktypeShowOut(BaseModel):
    data: Any

class TasktypeShowUpdate(BaseModel):
    data: Any

class TasktypeShowDb(BaseModel):
    data: Any

