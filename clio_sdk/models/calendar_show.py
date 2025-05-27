
from pydantic import BaseModel

from .calendar import CalendarOut


class CalendarShowIn(BaseModel):
    data: CalendarIn

class CalendarShowOut(BaseModel):
    data: CalendarOut

class CalendarShowUpdate(BaseModel):
    data: CalendarUpdate

class CalendarShowDb(BaseModel):
    data: CalendarDb

