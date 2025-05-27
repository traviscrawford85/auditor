from typing import Optional

from pydantic import BaseModel


class CalendarentrycreaterequestdataconferencemeetingIn(BaseModel):
    type: Optional[str] = None

class CalendarentrycreaterequestdataconferencemeetingOut(BaseModel):
    type: Optional[str] = None

class CalendarentrycreaterequestdataconferencemeetingUpdate(BaseModel):
    type: Optional[str] = None

class CalendarentrycreaterequestdataconferencemeetingDb(BaseModel):
    type: Optional[str] = None

