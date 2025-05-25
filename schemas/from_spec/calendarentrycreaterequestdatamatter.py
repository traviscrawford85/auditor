from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentrycreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

