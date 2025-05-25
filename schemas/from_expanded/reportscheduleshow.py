from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportscheduleShowIn(BaseModel):
    data: Any

class ReportscheduleShowOut(BaseModel):
    data: Any

class ReportscheduleShowUpdate(BaseModel):
    data: Any

class ReportscheduleShowDb(BaseModel):
    data: Any

