from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReportschedulecreaterequestdataIn(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: str
    report_preset_id: int
    time_of_day: datetime
    time_zone: str

class ReportschedulecreaterequestdataOut(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: str
    report_preset_id: int
    time_of_day: datetime
    time_zone: str

class ReportschedulecreaterequestdataUpdate(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: str
    report_preset_id: int
    time_of_day: datetime
    time_zone: str

class ReportschedulecreaterequestdataDb(BaseModel):
    day_of_month: Optional[str] = None
    days_of_week: Optional[str] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[str] = None
    frequency: str
    report_preset_id: int
    time_of_day: datetime
    time_zone: str

