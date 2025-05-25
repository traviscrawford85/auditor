from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EventmetricsShowIn(BaseModel):
    data: Any

class EventmetricsShowOut(BaseModel):
    data: Any

class EventmetricsShowUpdate(BaseModel):
    data: Any

class EventmetricsShowDb(BaseModel):
    data: Any

