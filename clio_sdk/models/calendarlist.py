from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarListIn(BaseModel):
    data: List[Calendar]

class CalendarListOut(BaseModel):
    data: List[Calendar]

class CalendarListUpdate(BaseModel):
    data: List[Calendar]

class CalendarListDb(BaseModel):
    data: List[Calendar]

