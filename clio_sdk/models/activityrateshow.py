from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityrateShowIn(BaseModel):
    data: Activityrate

class ActivityrateShowOut(BaseModel):
    data: Activityrate

class ActivityrateShowUpdate(BaseModel):
    data: Activityrate

class ActivityrateShowDb(BaseModel):
    data: Activityrate

