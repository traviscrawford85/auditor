from typing import Optional

from pydantic import BaseModel


class CalendarentryeventtypeIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

