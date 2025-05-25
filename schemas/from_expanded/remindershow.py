from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReminderShowIn(BaseModel):
    data: Any

class ReminderShowOut(BaseModel):
    data: Any

class ReminderShowUpdate(BaseModel):
    data: Any

class ReminderShowDb(BaseModel):
    data: Any

