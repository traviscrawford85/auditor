from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentrycreaterequestdataconferencemeetingIn(BaseModel):
    type: Optional[str] = None

class CalendarentrycreaterequestdataconferencemeetingOut(BaseModel):
    type: Optional[str] = None

class CalendarentrycreaterequestdataconferencemeetingUpdate(BaseModel):
    type: Optional[str] = None

class CalendarentrycreaterequestdataconferencemeetingDb(BaseModel):
    type: Optional[str] = None

