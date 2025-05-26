from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportscheduleBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    time_of_day: Optional[datetime] = None
    frequency: Optional[str] = None
    days_of_week: Optional[List[int]] = None
    day_of_month: Optional[int] = None
    status: Optional[str] = None
    status_updated_at: Optional[datetime] = None
    next_scheduled_date: Optional[datetime] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    every_no_of_months: Optional[int] = None
    effective_from: Optional[str] = None

class ReportscheduleBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    time_of_day: Optional[datetime] = None
    frequency: Optional[str] = None
    days_of_week: Optional[List[int]] = None
    day_of_month: Optional[int] = None
    status: Optional[str] = None
    status_updated_at: Optional[datetime] = None
    next_scheduled_date: Optional[datetime] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    every_no_of_months: Optional[int] = None
    effective_from: Optional[str] = None

class ReportscheduleBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    time_of_day: Optional[datetime] = None
    frequency: Optional[str] = None
    days_of_week: Optional[List[int]] = None
    day_of_month: Optional[int] = None
    status: Optional[str] = None
    status_updated_at: Optional[datetime] = None
    next_scheduled_date: Optional[datetime] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    every_no_of_months: Optional[int] = None
    effective_from: Optional[str] = None

class ReportscheduleBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    time_of_day: Optional[datetime] = None
    frequency: Optional[str] = None
    days_of_week: Optional[List[int]] = None
    day_of_month: Optional[int] = None
    status: Optional[str] = None
    status_updated_at: Optional[datetime] = None
    next_scheduled_date: Optional[datetime] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    every_no_of_months: Optional[int] = None
    effective_from: Optional[str] = None

