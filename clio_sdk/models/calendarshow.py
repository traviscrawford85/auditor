from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarShowIn(BaseModel):
    data: Calendar

class CalendarShowOut(BaseModel):
    data: Calendar

class CalendarShowUpdate(BaseModel):
    data: Calendar

class CalendarShowDb(BaseModel):
    data: Calendar

