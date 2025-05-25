from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityListIn(BaseModel):
    data: List[Any]

class ActivityListOut(BaseModel):
    data: List[Any]

class ActivityListUpdate(BaseModel):
    data: List[Any]

class ActivityListDb(BaseModel):
    data: List[Any]

