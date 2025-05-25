from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityCalendarentryBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[int] = None

class ActivityCalendarentryBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[int] = None

class ActivityCalendarentryBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[int] = None

class ActivityCalendarentryBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    calendar_owner_id: Optional[int] = None

