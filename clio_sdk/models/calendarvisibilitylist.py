from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarvisibilityListIn(BaseModel):
    data: List[Calendarvisibility]

class CalendarvisibilityListOut(BaseModel):
    data: List[Calendarvisibility]

class CalendarvisibilityListUpdate(BaseModel):
    data: List[Calendarvisibility]

class CalendarvisibilityListDb(BaseModel):
    data: List[Calendarvisibility]

