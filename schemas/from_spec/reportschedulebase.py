from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportschedulebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    time_of_day: Optional[str] = None
    frequency: Optional[str] = None
    days_of_week: Optional[str] = None
    day_of_month: Optional[str] = None
    status: Optional[str] = None
    status_updated_at: Optional[str] = None
    next_scheduled_date: Optional[str] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    every_no_of_months: Optional[str] = None
    effective_from: Optional[str] = None

class ReportschedulebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    time_of_day: Optional[str] = None
    frequency: Optional[str] = None
    days_of_week: Optional[str] = None
    day_of_month: Optional[str] = None
    status: Optional[str] = None
    status_updated_at: Optional[str] = None
    next_scheduled_date: Optional[str] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    every_no_of_months: Optional[str] = None
    effective_from: Optional[str] = None

class ReportschedulebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    time_of_day: Optional[str] = None
    frequency: Optional[str] = None
    days_of_week: Optional[str] = None
    day_of_month: Optional[str] = None
    status: Optional[str] = None
    status_updated_at: Optional[str] = None
    next_scheduled_date: Optional[str] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    every_no_of_months: Optional[str] = None
    effective_from: Optional[str] = None

class ReportschedulebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    time_of_day: Optional[str] = None
    frequency: Optional[str] = None
    days_of_week: Optional[str] = None
    day_of_month: Optional[str] = None
    status: Optional[str] = None
    status_updated_at: Optional[str] = None
    next_scheduled_date: Optional[str] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    every_no_of_months: Optional[str] = None
    effective_from: Optional[str] = None

