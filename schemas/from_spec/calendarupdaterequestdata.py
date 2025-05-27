from typing import Optional

from pydantic import BaseModel


class CalendarupdaterequestdataIn(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None
    source: Optional[str] = None
    visible: Optional[str] = None

class CalendarupdaterequestdataOut(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None
    source: Optional[str] = None
    visible: Optional[str] = None

class CalendarupdaterequestdataUpdate(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None
    source: Optional[str] = None
    visible: Optional[str] = None

class CalendarupdaterequestdataDb(BaseModel):
    color: Optional[str] = None
    name: Optional[str] = None
    source: Optional[str] = None
    visible: Optional[str] = None

