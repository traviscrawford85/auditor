from typing import List

from pydantic import BaseModel

from .activity import ActivityOut


class ActivityListIn(BaseModel):
    data: List[ActivityIn]

class ActivityListOut(BaseModel):
    data: List[ActivityOut]

class ActivityListUpdate(BaseModel):
    data: List[ActivityUpdate]

class ActivityListDb(BaseModel):
    data: List[ActivityDb]

