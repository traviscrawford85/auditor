from typing import Optional

from pydantic import BaseModel


class CalendarentrycreaterequestdataexternalpropertiesinnerIn(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class CalendarentrycreaterequestdataexternalpropertiesinnerOut(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class CalendarentrycreaterequestdataexternalpropertiesinnerUpdate(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class CalendarentrycreaterequestdataexternalpropertiesinnerDb(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

