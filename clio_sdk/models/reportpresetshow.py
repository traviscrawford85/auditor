from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportpresetShowIn(BaseModel):
    data: Reportpreset

class ReportpresetShowOut(BaseModel):
    data: Reportpreset

class ReportpresetShowUpdate(BaseModel):
    data: Reportpreset

class ReportpresetShowDb(BaseModel):
    data: Reportpreset

