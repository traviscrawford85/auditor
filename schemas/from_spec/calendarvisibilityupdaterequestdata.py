from typing import Optional

from pydantic import BaseModel


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

