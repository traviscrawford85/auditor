from typing import Optional

from pydantic import BaseModel


class CalendarentrycreaterequestdataattendeesinnerIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    _destroy: Optional[str] = None

class CalendarentrycreaterequestdataattendeesinnerOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    _destroy: Optional[str] = None

class CalendarentrycreaterequestdataattendeesinnerUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    _destroy: Optional[str] = None

class CalendarentrycreaterequestdataattendeesinnerDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    _destroy: Optional[str] = None

