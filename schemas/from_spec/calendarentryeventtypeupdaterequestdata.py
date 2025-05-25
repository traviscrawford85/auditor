from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryeventtypeupdaterequestdataIn(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeupdaterequestdataOut(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeupdaterequestdataUpdate(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeupdaterequestdataDb(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None

