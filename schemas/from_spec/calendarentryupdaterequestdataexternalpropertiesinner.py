from typing import Optional

from pydantic import BaseModel


class CalendarentryupdaterequestdataexternalpropertiesinnerIn(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class CalendarentryupdaterequestdataexternalpropertiesinnerOut(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class CalendarentryupdaterequestdataexternalpropertiesinnerUpdate(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

class CalendarentryupdaterequestdataexternalpropertiesinnerDb(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None
    _destroy: Optional[str] = None

