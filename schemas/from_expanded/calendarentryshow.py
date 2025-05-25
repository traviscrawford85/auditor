from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryShowIn(BaseModel):
    data: Any

class CalendarentryShowOut(BaseModel):
    data: Any

class CalendarentryShowUpdate(BaseModel):
    data: Any

class CalendarentryShowDb(BaseModel):
    data: Any

