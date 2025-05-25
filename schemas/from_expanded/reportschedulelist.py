from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportscheduleListIn(BaseModel):
    data: List[Any]

class ReportscheduleListOut(BaseModel):
    data: List[Any]

class ReportscheduleListUpdate(BaseModel):
    data: List[Any]

class ReportscheduleListDb(BaseModel):
    data: List[Any]

