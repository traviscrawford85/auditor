from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    all_day: Optional[str] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[str] = None
    court_rule: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[str] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[str] = None

class CalendarentryBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    all_day: Optional[str] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[str] = None
    court_rule: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[str] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[str] = None

class CalendarentryBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    all_day: Optional[str] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[str] = None
    court_rule: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[str] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[str] = None

class CalendarentryBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    all_day: Optional[str] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[str] = None
    court_rule: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[str] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[str] = None

