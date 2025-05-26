from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportscheduleShowIn(BaseModel):
    data: Reportschedule

class ReportscheduleShowOut(BaseModel):
    data: Reportschedule

class ReportscheduleShowUpdate(BaseModel):
    data: Reportschedule

class ReportscheduleShowDb(BaseModel):
    data: Reportschedule

