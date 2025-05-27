from typing import List

from pydantic import BaseModel

from .calendarvisibility import CalendarvisibilityOut


class CalendarvisibilityListIn(BaseModel):
    data: List[CalendarvisibilityIn]

class CalendarvisibilityListOut(BaseModel):
    data: List[CalendarvisibilityOut]

class CalendarvisibilityListUpdate(BaseModel):
    data: List[CalendarvisibilityUpdate]

class CalendarvisibilityListDb(BaseModel):
    data: List[CalendarvisibilityDb]

