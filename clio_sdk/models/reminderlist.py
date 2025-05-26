from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReminderListIn(BaseModel):
    data: List[Reminder]

class ReminderListOut(BaseModel):
    data: List[Reminder]

class ReminderListUpdate(BaseModel):
    data: List[Reminder]

class ReminderListDb(BaseModel):
    data: List[Reminder]

