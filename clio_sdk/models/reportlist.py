from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportListIn(BaseModel):
    data: List[Report]

class ReportListOut(BaseModel):
    data: List[Report]

class ReportListUpdate(BaseModel):
    data: List[Report]

class ReportListDb(BaseModel):
    data: List[Report]

