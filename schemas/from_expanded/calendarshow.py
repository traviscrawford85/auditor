from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarShowIn(BaseModel):
    data: Any

class CalendarShowOut(BaseModel):
    data: Any

class CalendarShowUpdate(BaseModel):
    data: Any

class CalendarShowDb(BaseModel):
    data: Any

