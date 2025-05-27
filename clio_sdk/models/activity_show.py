
from pydantic import BaseModel

from .activity import ActivityOut


class ActivityShowIn(BaseModel):
    data: ActivityIn

class ActivityShowOut(BaseModel):
    data: ActivityOut

class ActivityShowUpdate(BaseModel):
    data: ActivityUpdate

class ActivityShowDb(BaseModel):
    data: ActivityDb

