
from pydantic import BaseModel

from .calendarentry import CalendarentryOut


class CalendarentryShowIn(BaseModel):
    data: CalendarentryIn

class CalendarentryShowOut(BaseModel):
    data: CalendarentryOut

class CalendarentryShowUpdate(BaseModel):
    data: CalendarentryUpdate

class CalendarentryShowDb(BaseModel):
    data: CalendarentryDb

