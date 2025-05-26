from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TimerShowIn(BaseModel):
    data: Timer

class TimerShowOut(BaseModel):
    data: Timer

class TimerShowUpdate(BaseModel):
    data: Timer

class TimerShowDb(BaseModel):
    data: Timer

