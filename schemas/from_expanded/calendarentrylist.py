from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryListIn(BaseModel):
    data: List[Any]

class CalendarentryListOut(BaseModel):
    data: List[Any]

class CalendarentryListUpdate(BaseModel):
    data: List[Any]

class CalendarentryListDb(BaseModel):
    data: List[Any]

