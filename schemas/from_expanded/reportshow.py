from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportShowIn(BaseModel):
    data: Any

class ReportShowOut(BaseModel):
    data: Any

class ReportShowUpdate(BaseModel):
    data: Any

class ReportShowDb(BaseModel):
    data: Any

