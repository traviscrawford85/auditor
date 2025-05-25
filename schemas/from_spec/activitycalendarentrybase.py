from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitycalendarentrybaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

class ActivitycalendarentrybaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

class ActivitycalendarentrybaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

class ActivitycalendarentrybaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

