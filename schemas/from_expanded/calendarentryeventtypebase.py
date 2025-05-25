from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryeventtypeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    color: Optional[str] = None
    name: Optional[str] = None

