from typing import List

from pydantic import BaseModel

from .reportschedule import ReportscheduleOut


class ReportscheduleListIn(BaseModel):
    data: List[ReportscheduleIn]

class ReportscheduleListOut(BaseModel):
    data: List[ReportscheduleOut]

class ReportscheduleListUpdate(BaseModel):
    data: List[ReportscheduleUpdate]

class ReportscheduleListDb(BaseModel):
    data: List[ReportscheduleDb]

