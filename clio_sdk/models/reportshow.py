from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportShowIn(BaseModel):
    data: Report

class ReportShowOut(BaseModel):
    data: Report

class ReportShowUpdate(BaseModel):
    data: Report

class ReportShowDb(BaseModel):
    data: Report

