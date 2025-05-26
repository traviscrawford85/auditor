from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryShowIn(BaseModel):
    data: Calendarentry

class CalendarentryShowOut(BaseModel):
    data: Calendarentry

class CalendarentryShowUpdate(BaseModel):
    data: Calendarentry

class CalendarentryShowDb(BaseModel):
    data: Calendarentry

