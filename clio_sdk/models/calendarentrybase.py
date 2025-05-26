from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarentryBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    all_day: Optional[bool] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[int] = None
    court_rule: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[int] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[int] = None

class CalendarentryBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    all_day: Optional[bool] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[int] = None
    court_rule: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[int] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[int] = None

class CalendarentryBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    all_day: Optional[bool] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[int] = None
    court_rule: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[int] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[int] = None

class CalendarentryBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    all_day: Optional[bool] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[int] = None
    court_rule: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[int] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[int] = None

