
from pydantic import BaseModel

from .eventmetrics import EventmetricsOut


class EventmetricsShowIn(BaseModel):
    data: EventmetricsIn

class EventmetricsShowOut(BaseModel):
    data: EventmetricsOut

class EventmetricsShowUpdate(BaseModel):
    data: EventmetricsUpdate

class EventmetricsShowDb(BaseModel):
    data: EventmetricsDb

