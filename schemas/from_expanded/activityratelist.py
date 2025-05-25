from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityrateListIn(BaseModel):
    data: List[Any]

class ActivityrateListOut(BaseModel):
    data: List[Any]

class ActivityrateListUpdate(BaseModel):
    data: List[Any]

class ActivityrateListDb(BaseModel):
    data: List[Any]

