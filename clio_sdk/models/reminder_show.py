
from pydantic import BaseModel

from .reminder import ReminderOut


class ReminderShowIn(BaseModel):
    data: ReminderIn

class ReminderShowOut(BaseModel):
    data: ReminderOut

class ReminderShowUpdate(BaseModel):
    data: ReminderUpdate

class ReminderShowDb(BaseModel):
    data: ReminderDb

