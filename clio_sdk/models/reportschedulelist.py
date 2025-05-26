from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportscheduleListIn(BaseModel):
    data: List[Reportschedule]

class ReportscheduleListOut(BaseModel):
    data: List[Reportschedule]

class ReportscheduleListUpdate(BaseModel):
    data: List[Reportschedule]

class ReportscheduleListDb(BaseModel):
    data: List[Reportschedule]

