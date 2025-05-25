from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryeventtypebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

class CalendarentryeventtypebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

