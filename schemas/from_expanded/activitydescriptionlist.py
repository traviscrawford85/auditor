from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitydescriptionListIn(BaseModel):
    data: List[Any]

class ActivitydescriptionListOut(BaseModel):
    data: List[Any]

class ActivitydescriptionListUpdate(BaseModel):
    data: List[Any]

class ActivitydescriptionListDb(BaseModel):
    data: List[Any]

