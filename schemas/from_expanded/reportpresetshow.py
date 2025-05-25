from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportpresetShowIn(BaseModel):
    data: Any

class ReportpresetShowOut(BaseModel):
    data: Any

class ReportpresetShowUpdate(BaseModel):
    data: Any

class ReportpresetShowDb(BaseModel):
    data: Any

