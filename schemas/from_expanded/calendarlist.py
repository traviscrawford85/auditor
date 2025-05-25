from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarListIn(BaseModel):
    data: List[Any]

class CalendarListOut(BaseModel):
    data: List[Any]

class CalendarListUpdate(BaseModel):
    data: List[Any]

class CalendarListDb(BaseModel):
    data: List[Any]

