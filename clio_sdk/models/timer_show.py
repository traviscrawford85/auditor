
from pydantic import BaseModel

from .timer import TimerOut


class TimerShowIn(BaseModel):
    data: TimerIn

class TimerShowOut(BaseModel):
    data: TimerOut

class TimerShowUpdate(BaseModel):
    data: TimerUpdate

class TimerShowDb(BaseModel):
    data: TimerDb

