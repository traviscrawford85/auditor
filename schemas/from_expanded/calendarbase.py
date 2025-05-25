from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[bool] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    source: Optional[str] = None

class CalendarBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[bool] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    source: Optional[str] = None

class CalendarBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[bool] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    source: Optional[str] = None

class CalendarBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[bool] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    source: Optional[str] = None

