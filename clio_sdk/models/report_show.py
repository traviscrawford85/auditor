
from pydantic import BaseModel

from .report import ReportOut


class ReportShowIn(BaseModel):
    data: ReportIn

class ReportShowOut(BaseModel):
    data: ReportOut

class ReportShowUpdate(BaseModel):
    data: ReportUpdate

class ReportShowDb(BaseModel):
    data: ReportDb

