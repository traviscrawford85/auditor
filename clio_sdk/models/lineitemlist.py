from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemListIn(BaseModel):
    data: List[Lineitem]

class LineitemListOut(BaseModel):
    data: List[Lineitem]

class LineitemListUpdate(BaseModel):
    data: List[Lineitem]

class LineitemListDb(BaseModel):
    data: List[Lineitem]

