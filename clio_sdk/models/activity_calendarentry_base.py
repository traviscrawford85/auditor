from typing import Optional

from pydantic import BaseModel


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

