from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportListIn(BaseModel):
    data: List[Any]

class ReportListOut(BaseModel):
    data: List[Any]

class ReportListUpdate(BaseModel):
    data: List[Any]

class ReportListDb(BaseModel):
    data: List[Any]

