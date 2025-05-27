from typing import List

from pydantic import BaseModel

from .reportpreset import ReportpresetOut


class ReportpresetListIn(BaseModel):
    data: List[ReportpresetIn]

class ReportpresetListOut(BaseModel):
    data: List[ReportpresetOut]

class ReportpresetListUpdate(BaseModel):
    data: List[ReportpresetUpdate]

class ReportpresetListDb(BaseModel):
    data: List[ReportpresetDb]

