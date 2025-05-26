from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitycalendarentryBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

class ActivitycalendarentryBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

class ActivitycalendarentryBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

class ActivitycalendarentryBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[str] = None

