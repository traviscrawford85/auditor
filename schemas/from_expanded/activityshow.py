from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityShowIn(BaseModel):
    data: Any

class ActivityShowOut(BaseModel):
    data: Any

class ActivityShowUpdate(BaseModel):
    data: Any

class ActivityShowDb(BaseModel):
    data: Any

