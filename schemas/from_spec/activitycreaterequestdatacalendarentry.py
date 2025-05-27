from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdatacalendarentryIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacalendarentryOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacalendarentryUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdatacalendarentryDb(BaseModel):
    id: Optional[str] = None

