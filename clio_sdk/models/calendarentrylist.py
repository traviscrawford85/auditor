from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryListIn(BaseModel):
    data: List[Calendarentry]

class CalendarentryListOut(BaseModel):
    data: List[Calendarentry]

class CalendarentryListUpdate(BaseModel):
    data: List[Calendarentry]

class CalendarentryListDb(BaseModel):
    data: List[Calendarentry]

