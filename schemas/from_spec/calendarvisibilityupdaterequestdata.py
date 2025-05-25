from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarvisibilityupdaterequestdataIn(BaseModel):
    color: Optional[str] = None
    visible: Optional[str] = None

class CalendarvisibilityupdaterequestdataOut(BaseModel):
    color: Optional[str] = None
    visible: Optional[str] = None

class CalendarvisibilityupdaterequestdataUpdate(BaseModel):
    color: Optional[str] = None
    visible: Optional[str] = None

class CalendarvisibilityupdaterequestdataDb(BaseModel):
    color: Optional[str] = None
    visible: Optional[str] = None

