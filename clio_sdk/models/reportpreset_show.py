
from pydantic import BaseModel

from .reportpreset import ReportpresetOut


class ReportpresetShowIn(BaseModel):
    data: ReportpresetIn

class ReportpresetShowOut(BaseModel):
    data: ReportpresetOut

class ReportpresetShowUpdate(BaseModel):
    data: ReportpresetUpdate

class ReportpresetShowDb(BaseModel):
    data: ReportpresetDb

