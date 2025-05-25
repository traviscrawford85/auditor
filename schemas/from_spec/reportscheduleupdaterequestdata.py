from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportscheduleupdaterequestdataIn(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: Optional[str] = None
    report_preset_id: Optional[str] = None
    time_of_day: Optional[str] = None
    time_zone: Optional[str] = None

class ReportscheduleupdaterequestdataOut(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: Optional[str] = None
    report_preset_id: Optional[str] = None
    time_of_day: Optional[str] = None
    time_zone: Optional[str] = None

class ReportscheduleupdaterequestdataUpdate(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: Optional[str] = None
    report_preset_id: Optional[str] = None
    time_of_day: Optional[str] = None
    time_zone: Optional[str] = None

class ReportscheduleupdaterequestdataDb(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: Optional[str] = None
    report_preset_id: Optional[str] = None
    time_of_day: Optional[str] = None
    time_zone: Optional[str] = None

