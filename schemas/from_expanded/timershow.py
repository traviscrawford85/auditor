from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TimerShowIn(BaseModel):
    data: Any

class TimerShowOut(BaseModel):
    data: Any

class TimerShowUpdate(BaseModel):
    data: Any

class TimerShowDb(BaseModel):
    data: Any

