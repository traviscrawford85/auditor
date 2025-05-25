from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarvisibilityListIn(BaseModel):
    data: List[Any]

class CalendarvisibilityListOut(BaseModel):
    data: List[Any]

class CalendarvisibilityListUpdate(BaseModel):
    data: List[Any]

class CalendarvisibilityListDb(BaseModel):
    data: List[Any]

