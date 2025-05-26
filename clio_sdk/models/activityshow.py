from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityShowIn(BaseModel):
    data: Activity

class ActivityShowOut(BaseModel):
    data: Activity

class ActivityShowUpdate(BaseModel):
    data: Activity

class ActivityShowDb(BaseModel):
    data: Activity

