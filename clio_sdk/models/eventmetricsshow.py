from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EventmetricsShowIn(BaseModel):
    data: Eventmetrics

class EventmetricsShowOut(BaseModel):
    data: Eventmetrics

class EventmetricsShowUpdate(BaseModel):
    data: Eventmetrics

class EventmetricsShowDb(BaseModel):
    data: Eventmetrics

