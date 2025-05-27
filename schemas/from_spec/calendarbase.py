from typing import Optional

from pydantic import BaseModel


class CalendarBaseIn(BaseModel):
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

class CalendarBaseOut(BaseModel):
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

class CalendarBaseUpdate(BaseModel):
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

class CalendarBaseDb(BaseModel):
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

