from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LogentryListIn(BaseModel):
    data: List[Any]

class LogentryListOut(BaseModel):
    data: List[Any]

class LogentryListUpdate(BaseModel):
    data: List[Any]

class LogentryListDb(BaseModel):
    data: List[Any]

