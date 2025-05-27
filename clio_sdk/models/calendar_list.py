from typing import List

from pydantic import BaseModel

from .calendar import CalendarOut


class CalendarListIn(BaseModel):
    data: List[CalendarIn]

class CalendarListOut(BaseModel):
    data: List[CalendarOut]

class CalendarListUpdate(BaseModel):
    data: List[CalendarUpdate]

class CalendarListDb(BaseModel):
    data: List[CalendarDb]

