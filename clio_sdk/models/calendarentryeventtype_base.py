from typing import Optional

from pydantic import BaseModel


class CalendarentryeventtypeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

