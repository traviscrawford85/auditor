from typing import List

from pydantic import BaseModel

from .logentry import LogentryOut


class LogentryListIn(BaseModel):
    data: List[LogentryIn]

class LogentryListOut(BaseModel):
    data: List[LogentryOut]

class LogentryListUpdate(BaseModel):
    data: List[LogentryUpdate]

class LogentryListDb(BaseModel):
    data: List[LogentryDb]

