from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportpresetListIn(BaseModel):
    data: List[Any]

class ReportpresetListOut(BaseModel):
    data: List[Any]

class ReportpresetListUpdate(BaseModel):
    data: List[Any]

class ReportpresetListDb(BaseModel):
    data: List[Any]

