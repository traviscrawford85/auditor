from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarvisibilityShowIn(BaseModel):
    data: Calendarvisibility

class CalendarvisibilityShowOut(BaseModel):
    data: Calendarvisibility

class CalendarvisibilityShowUpdate(BaseModel):
    data: Calendarvisibility

class CalendarvisibilityShowDb(BaseModel):
    data: Calendarvisibility

