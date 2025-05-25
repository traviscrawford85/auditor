from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemListIn(BaseModel):
    data: List[Any]

class LineitemListOut(BaseModel):
    data: List[Any]

class LineitemListUpdate(BaseModel):
    data: List[Any]

class LineitemListDb(BaseModel):
    data: List[Any]

