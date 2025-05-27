from typing import List

from pydantic import BaseModel

from .report import ReportOut


class ReportListIn(BaseModel):
    data: List[ReportIn]

class ReportListOut(BaseModel):
    data: List[ReportOut]

class ReportListUpdate(BaseModel):
    data: List[ReportUpdate]

class ReportListDb(BaseModel):
    data: List[ReportDb]

