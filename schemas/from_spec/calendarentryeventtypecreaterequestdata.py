from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryeventtypecreaterequestdataIn(BaseModel):
    color: str
    name: str

class CalendarentryeventtypecreaterequestdataOut(BaseModel):
    color: str
    name: str

class CalendarentryeventtypecreaterequestdataUpdate(BaseModel):
    color: str
    name: str

class CalendarentryeventtypecreaterequestdataDb(BaseModel):
    color: str
    name: str

