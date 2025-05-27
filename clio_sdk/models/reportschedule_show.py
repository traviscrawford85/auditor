
from pydantic import BaseModel

from .reportschedule import ReportscheduleOut


class ReportscheduleShowIn(BaseModel):
    data: ReportscheduleIn

class ReportscheduleShowOut(BaseModel):
    data: ReportscheduleOut

class ReportscheduleShowUpdate(BaseModel):
    data: ReportscheduleUpdate

class ReportscheduleShowDb(BaseModel):
    data: ReportscheduleDb

