from typing import Optional

from pydantic import BaseModel


class CalendarentrycreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class CalendarentrycreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

