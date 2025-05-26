from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityrateListIn(BaseModel):
    data: List[Activityrate]

class ActivityrateListOut(BaseModel):
    data: List[Activityrate]

class ActivityrateListUpdate(BaseModel):
    data: List[Activityrate]

class ActivityrateListDb(BaseModel):
    data: List[Activityrate]

