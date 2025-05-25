from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[str] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    source: Optional[str] = None

class CalendarbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[str] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    source: Optional[str] = None

class CalendarbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[str] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    source: Optional[str] = None

class CalendarbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[str] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    source: Optional[str] = None

