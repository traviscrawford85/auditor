from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReminderListIn(BaseModel):
    data: List[Any]

class ReminderListOut(BaseModel):
    data: List[Any]

class ReminderListUpdate(BaseModel):
    data: List[Any]

class ReminderListDb(BaseModel):
    data: List[Any]

