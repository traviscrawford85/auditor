from typing import List

from pydantic import BaseModel

from .activityrate import ActivityrateOut


class ActivityrateListIn(BaseModel):
    data: List[ActivityrateIn]

class ActivityrateListOut(BaseModel):
    data: List[ActivityrateOut]

class ActivityrateListUpdate(BaseModel):
    data: List[ActivityrateUpdate]

class ActivityrateListDb(BaseModel):
    data: List[ActivityrateDb]

