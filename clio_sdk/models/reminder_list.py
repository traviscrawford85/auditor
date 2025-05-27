from typing import List

from pydantic import BaseModel

from .reminder import ReminderOut


class ReminderListIn(BaseModel):
    data: List[ReminderIn]

class ReminderListOut(BaseModel):
    data: List[ReminderOut]

class ReminderListUpdate(BaseModel):
    data: List[ReminderUpdate]

class ReminderListDb(BaseModel):
    data: List[ReminderDb]

