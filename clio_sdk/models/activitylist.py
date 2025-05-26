from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityListIn(BaseModel):
    data: List[Activity]

class ActivityListOut(BaseModel):
    data: List[Activity]

class ActivityListUpdate(BaseModel):
    data: List[Activity]

class ActivityListDb(BaseModel):
    data: List[Activity]

