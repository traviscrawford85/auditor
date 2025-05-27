from typing import List

from pydantic import BaseModel

from .calendarentry import CalendarentryOut


class CalendarentryListIn(BaseModel):
    data: List[CalendarentryIn]

class CalendarentryListOut(BaseModel):
    data: List[CalendarentryOut]

class CalendarentryListUpdate(BaseModel):
    data: List[CalendarentryUpdate]

class CalendarentryListDb(BaseModel):
    data: List[CalendarentryDb]

