from typing import Optional

from pydantic import BaseModel


class CalendarentrycreaterequestdatacalendarentryeventtypeIn(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatacalendarentryeventtypeOut(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatacalendarentryeventtypeUpdate(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatacalendarentryeventtypeDb(BaseModel):
    id: Optional[str] = None

