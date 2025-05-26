from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportpresetListIn(BaseModel):
    data: List[Reportpreset]

class ReportpresetListOut(BaseModel):
    data: List[Reportpreset]

class ReportpresetListUpdate(BaseModel):
    data: List[Reportpreset]

class ReportpresetListDb(BaseModel):
    data: List[Reportpreset]

