
from pydantic import BaseModel

from .calendarvisibility import CalendarvisibilityOut


class CalendarvisibilityShowIn(BaseModel):
    data: CalendarvisibilityIn

class CalendarvisibilityShowOut(BaseModel):
    data: CalendarvisibilityOut

class CalendarvisibilityShowUpdate(BaseModel):
    data: CalendarvisibilityUpdate

class CalendarvisibilityShowDb(BaseModel):
    data: CalendarvisibilityDb

