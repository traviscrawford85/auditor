from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LogentryListIn(BaseModel):
    data: List[Logentry]

class LogentryListOut(BaseModel):
    data: List[Logentry]

class LogentryListUpdate(BaseModel):
    data: List[Logentry]

class LogentryListDb(BaseModel):
    data: List[Logentry]

