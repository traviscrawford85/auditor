from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReminderShowIn(BaseModel):
    data: Reminder

class ReminderShowOut(BaseModel):
    data: Reminder

class ReminderShowUpdate(BaseModel):
    data: Reminder

class ReminderShowDb(BaseModel):
    data: Reminder

